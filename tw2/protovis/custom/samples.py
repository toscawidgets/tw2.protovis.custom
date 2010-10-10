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
