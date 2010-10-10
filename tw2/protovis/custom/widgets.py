"""
TODO
"""

import tw2.core as twc
import tw2.protovis.core as twp
from tw2.protovis.core import pv

class js(twc.JSSymbol):
    def __init__(self, src):
        super(js, self).__init__(src=src)

class StreamGraph(twp.PVWidget):
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
