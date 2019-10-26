#! /usr/bin/python

import sys

data = sys.stdin.readline()

variable = data[43]
seq = data[58:].find('=')
wl = data[58:].find('where')
eq = data[58:58 + wl - 2]

s1 = data[58 + wl + 6]
cl = data[58 + wl + 6:].find(',')
v1 = data[58 + wl + 6 + 4:58 + wl + 6 + cl]
s2 = data[58 + wl + 6 + cl + 2]
v2 = data[58 + wl + 6 + cl + 6:-1]

eq = (eq.replace(s1, '*' + v1).replace(s2, '*' + v2).replace(variable, '*' + variable).replace('=', '-'))

print('''
from sympy.solvers import solve
from sympy import Symbol

%s = Symbol('%s')
print(solve('%s')[0])
''' % (variable, variable, eq))
