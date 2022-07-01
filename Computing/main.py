# -*- coding: utf-8 -*-

from computing.components import logicgates

n = logicgates.OR()
print(n.input, n.output)
n.input = [0, 0]
n.operate()
print(n.output)
