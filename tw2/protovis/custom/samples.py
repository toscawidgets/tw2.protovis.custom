""" Samples of how to use tw2.jit

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import (
    SparkLine,
    SparkBar,
    StreamGraph,
    BubbleChart,
)
from widgets import js
from tw2.core import JSSymbol

import math
import random

class DemoSparkLine(SparkLine):
    p_height = 10
    p_data = [
          40, 115, 100, 80, 60, 40, 23, 10, 10, 25, 75, 145,
          130, 130, 80, 65, 20, 10, 5, 10, 60, 190, 180, 175,
          120, 50, 35, 20, 10, 15, 30, 60, 105, 105, 105, 80, 65
    ]

class DemoSparkBar(SparkBar):
    p_height = 10
    p_data = [0.2, 0.3, 0.6, 0.1, 0.9, 0.8, 0.23, 0.77, 0.63, 0.43, 0.59, 0.11]

# The following are some data generation functions used by the streamgraph demo
def waves(n, m):
    def f(i, j):
        x = 20 * j / m - i / 3
        if x > 0:
            return 2 * x * math.exp(x * -0.5)
        return 0
    return map(lambda i : map(lambda j : f(i, j), range(m)), range(n))

def layers(n, m):
    def bump(a):
        x = 1.0 / (.1 + random.random())
        y = 2.0 * random.random() - 0.5
        z = 10.0 / (0.1 + random.random())
        for i in range(m):
            w = (float(i) / m - y) * z
            a[i] += x * math.exp(-w * w)
        return a
    def f(*args):
        a = [0] * m
        for i in range(5):
            a = bump(a)
        return a
    return map(f, range(n))

class DemoStreamGraph(StreamGraph):
    def prepare(self):
        self.p_data = layers(20, 400)
        super(DemoStreamGraph, self).prepare()

class DemoBubbleChart(BubbleChart):
    p_height = 500
    p_width = 500
    def prepare(self):
        self.p_data = {
          'analytics': {
            'cluster': {
              'AgglomerativeCluster': 3938,
              'CommunityStructure': 3812,
              'HierarchicalCluster': 6714,
              'MergeEdge': 743
            },
            'graph': {
              'BetweennessCentrality': 3534,
              'LinkDistance': 5731,
              'MaxFlowMinCut': 7840,
              'ShortestPaths': 5914,
              'SpanningTree': 3416
            },
            'optimization': {
              'AspectRatioBanker': 7074
            }
          },
          'animate': {
            'Easing': 17010,
            'FunctionSequence': 5842,
            'interpolate': {
              'ArrayInterpolator': 1983,
              'ColorInterpolator': 2047,
              'DateInterpolator': 1375,
              'Interpolator': 8746,
              'MatrixInterpolator': 2202,
              'NumberInterpolator': 1382,
              'ObjectInterpolator': 1629,
              'PointInterpolator': 1675,
              'RectangleInterpolator': 2042
            },
            'ISchedulable': 1041,
            'Parallel': 5176,
            'Pause': 449,
            'Scheduler': 5593,
            'Sequence': 5534,
            'Transition': 9201,
            'Transitioner': 19975,
            'TransitionEvent': 1116,
            'Tween': 6006
          },
          'data': {
            'converters': {
              'Converters': 721,
              'DelimitedTextConverter': 4294,
              'GraphMLConverter': 9800,
              'IDataConverter': 1314,
              'JSONConverter': 2220
            },
            'DataField': 1759,
            'DataSchema': 2165,
            'DataSet': 586,
            'DataSource': 3331,
            'DataTable': 772,
            'DataUtil': 3322
          },
          'display': {
            'DirtySprite': 8833,
            'LineSprite': 1732,
            'RectSprite': 3623,
            'TextSprite': 10066
          },
          'flex': {
            'FlareVis': 4116
          },
          'physics': {
            'DragForce': 1082,
            'GravityForce': 1336,
            'IForce': 319,
            'NBodyForce': 10498,
            'Particle': 2822,
            'Simulation': 9983,
            'Spring': 2213,
            'SpringForce': 1681
          },
          'query': {
            'AggregateExpression': 1616,
            'And': 1027,
            'Arithmetic': 3891,
            'Average': 891,
            'BinaryExpression': 2893,
            'Comparison': 5103,
            'CompositeExpression': 3677,
            'Count': 781,
            'DateUtil': 4141,
            'Distinct': 933,
            'Expression': 5130,
            'ExpressionIterator': 3617,
            'Fn': 3240,
            'If': 2732,
            'IsA': 2039,
            'Literal': 1214,
            'Match': 3748,
            'Maximum': 843,
            'methods': {
              'add': 593,
              'and': 330,
              'average': 287,
              'count': 277,
              'distinct': 292,
              'div': 595,
              'eq': 594,
              'fn': 460,
              'gt': 603,
              'gte': 625,
              'iff': 748,
              'isa': 461,
              'lt': 597,
              'lte': 619,
              'max': 283,
              'min': 283,
              'mod': 591,
              'mul': 603,
              'neq': 599,
              'not': 386,
              'or': 323,
              'orderby': 307,
              'range': 772,
              'select': 296,
              'stddev': 363,
              'sub': 600,
              'sum': 280,
              'update': 307,
              'variance': 335,
              'where': 299,
              'xor': 354,
              '_': 264
            },
            'Minimum': 843,
            'Not': 1554,
            'Or': 970,
            'Query': 13896,
            'Range': 1594,
            'StringUtil': 4130,
            'Sum': 791,
            'Variable': 1124,
            'Variance': 1876,
            'Xor': 1101
          },
          'scale': {
            'IScaleMap': 2105,
            'LinearScale': 1316,
            'LogScale': 3151,
            'OrdinalScale': 3770,
            'QuantileScale': 2435,
            'QuantitativeScale': 4839,
            'RootScale': 1756,
            'Scale': 4268,
            'ScaleType': 1821,
            'TimeScale': 5833
          },
          'util': {
            'Arrays': 8258,
            'Colors': 10001,
            'Dates': 8217,
            'Displays': 12555,
            'Filter': 2324,
            'Geometry': 10993,
            'heap': {
              'FibonacciHeap': 9354,
              'HeapNode': 1233
            },
            'IEvaluable': 335,
            'IPredicate': 383,
            'IValueProxy': 874,
            'math': {
              'DenseMatrix': 3165,
              'IMatrix': 2815,
              'SparseMatrix': 3366
            },
            'Maths': 17705,
            'Orientation': 1486,
            'palette': {
              'ColorPalette': 6367,
              'Palette': 1229,
              'ShapePalette': 2059,
              'SizePalette': 2291
            },
            'Property': 5559,
            'Shapes': 19118,
            'Sort': 6887,
            'Stats': 6557,
            'Strings': 22026
          },
          'vis': {
            'axis': {
              'Axes': 1302,
              'Axis': 24593,
              'AxisGridLine': 652,
              'AxisLabel': 636,
              'CartesianAxes': 6703
            },
            'controls': {
              'AnchorControl': 2138,
              'ClickControl': 3824,
              'Control': 1353,
              'ControlList': 4665,
              'DragControl': 2649,
              'ExpandControl': 2832,
              'HoverControl': 4896,
              'IControl': 763,
              'PanZoomControl': 5222,
              'SelectionControl': 7862,
              'TooltipControl': 8435
            },
            'data': {
              'Data': 20544,
              'DataList': 19788,
              'DataSprite': 10349,
              'EdgeSprite': 3301,
              'NodeSprite': 19382,
              'render': {
                'ArrowType': 698,
                'EdgeRenderer': 5569,
                'IRenderer': 353,
                'ShapeRenderer': 2247
              },
              'ScaleBinding': 11275,
              'Tree': 7147,
              'TreeBuilder': 9930
            },
            'events': {
              'DataEvent': 2313,
              'SelectionEvent': 1880,
              'TooltipEvent': 1701,
              'VisualizationEvent': 1117
            },
            'legend': {
              'Legend': 20859,
              'LegendItem': 4614,
              'LegendRange': 10530
            },
            'operator': {
              'distortion': {
                'BifocalDistortion': 4461,
                'Distortion': 6314,
                'FisheyeDistortion': 3444
              },
              'encoder': {
                'ColorEncoder': 3179,
                'Encoder': 4060,
                'PropertyEncoder': 4138,
                'ShapeEncoder': 1690,
                'SizeEncoder': 1830
              },
              'filter': {
                'FisheyeTreeFilter': 5219,
                'GraphDistanceFilter': 3165,
                'VisibilityFilter': 3509
              },
              'IOperator': 1286,
              'label': {
                'Labeler': 9956,
                'RadialLabeler': 3899,
                'StackedAreaLabeler': 3202
              },
              'layout': {
                'AxisLayout': 6725,
                'BundledEdgeRouter': 3727,
                'CircleLayout': 9317,
                'CirclePackingLayout': 12003,
                'DendrogramLayout': 4853,
                'ForceDirectedLayout': 8411,
                'IcicleTreeLayout': 4864,
                'IndentedTreeLayout': 3174,
                'Layout': 7881,
                'NodeLinkTreeLayout': 12870,
                'PieLayout': 2728,
                'RadialTreeLayout': 12348,
                'RandomLayout': 870,
                'StackedAreaLayout': 9121,
                'TreeMapLayout': 9191
              },
              'Operator': 2490,
              'OperatorList': 5248,
              'OperatorSequence': 4190,
              'OperatorSwitch': 2581,
              'SortOperator': 2023
            },
            'Visualization': 16540
          }
        }
        super(DemoBubbleChart, self).prepare()

