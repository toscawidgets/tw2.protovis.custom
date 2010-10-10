"""
TODO
"""

import tw2.core as twc
import tw2.protovis.core as twp
from tw2.protovis.core import pv

class js(twc.JSSymbol):
    def __init__(self, src):
        super(js, self).__init__(src=src)

class SparkLine(twp.PVWidget):
    """
    A sparkline is a word-sized data visualization, allowing visual
    representations of data to be embedded directly in prose. This avoids
    any interruption in the flow of text, with the data presented in
    descriptive context. Sparklines can be used where space is limited,
    unlike standalone figures.
    """
    p_dots = twc.Param('dots', default=False)

    def prepare(self):
        self.init_js = js(
            """
            var dots = %i;
            var data = %s;
            var n = data.length;
            var w = n,
                h = %i,
                min = pv.min.index(data),
                max = pv.max.index(data);
            """ % (self.p_dots, self.p_data, self.p_height))
       
        self.p_width = len(self.p_data)
        self.setupRootPanel()
        self.margin(2)

        self.add(pv.Line) \
          .data(js('data')) \
          .left(js('pv.Scale.linear(0, n - 1).range(0, w).by(pv.index)')) \
          .bottom(js('pv.Scale.linear(data).range(0, h)')) \
          .strokeStyle("#000") \
          .lineWidth(1) \
        .add(pv.Dot) \
          .visible(
              js('function() (dots && this.index==0) || this.index==n - 1')) \
          .strokeStyle(None) \
          .fillStyle("brown") \
          .radius(2) \
        .add(pv.Dot) \
          .visible(
              js('function() dots && (this.index==min || this.index==max)')) \
          .fillStyle("steelblue");

class SparkBar(twp.PVWidget):
    """ A sparkbar is just like a sparkline, but,... you know. """
    def prepare(self):
        self.init_js = js(
            """
            var data = %s;
            var n = data.length;
            var w = n,
                h = %i,
            """ % (self.p_data, self.p_height))
       
        self.setupRootPanel()

        self.add(pv.Bar) \
          .data(js('data'))\
          .width(4)\
          .left(js('function() 5 * this.index'))\
          .height(js('function(d) Math.round(h * d)'))\
          .bottom(0)

class StreamGraph(twp.PVWidget):
    """
    Streamgraphs are a generalization of stacked area graphs where the
    baseline is free. By shifting the baseline, it is possible to minimize
    the change in slope (or "wiggle") in individual series, thereby making
    it easier to perceive the thickness of any given layer across the data.
    Byron & Wattenberg describe several streamgraph algorithms in "Stacked
    Graphs--Geometry & Aesthetics", several of which are implemented by
    pv.Layout.Stack.
    """
    def prepare(self):
        self.init_js = js(
            """
            var n = 20, m = 400;
            var data = %s,
                w = %i,
                h = %i,
                x = pv.Scale.linear(0, m - 1).range(0, w),
                y = pv.Scale.linear(0, 2 * n).range(0, h);
            """ % (self.p_data, self.p_width, self.p_height))
        
        self.setupRootPanel()

        self.add(pv.Layout.Stack)\
                .layers(js('data'))\
                .order('inside-out')\
                .offset('wiggle')\
                .x(js('x.by(pv.index)'))\
                .y(js('y'))\
              .layer.add(pv.Area)\
                .fillStyle(js('pv.ramp("#aad", "#556").by(Math.random)'))\
                .strokeStyle(js('function() this.fillStyle().alpha(0.5)'))
