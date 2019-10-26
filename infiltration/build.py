#! /usr/bin/python

import sys

for line in sys.stdin:
    if 'convert' in line:
        break;

print("""def convert(init):
    value = ""
""")
for i in range(5):
    sys.stdin.readline()

for i in range(7):
    data = sys.stdin.readline()
    op = data[19]
    sys.stdin.readline()
    data = sys.stdin.readline()
    v1 = data[-4:-2]
    sys.stdin.readline()
    data = sys.stdin.readline()
    v2 = data[-4:-2]
    print("""
    if len(str(init)) {} {}:
        if int(str(init)[{}]) % 2 == 0:
            value += "{}"
        else:
            value += "{}"
    """.format(op, i, i, v1, v2))

print(
"""
    if len(str(init)) < 7:
        return value
""")
sys.stdin.readline()
sys.stdin.readline()

line = ''
for line in sys.stdin:
    if 'if' in line:
        idx = line[line.find('[') + 1: line.find(']')]
        i1 = line[line.find('"') + 1]
        data = sys.stdin.readline()
        v1 = data[-4:-2]
        data = sys.stdin.readline()
        data = sys.stdin.readline()
        v2 = data[-4:-2]
        print("""
    if value[{}] < "{}":
        value += "{}"
    else:
        value += "{}"
        """.format(idx, i1, v1, v2))
    else:
        break

print('    value = {}'.format(line[line.find('=')+2:-1]))
for line in sys.stdin:
    if '=' not in line:
        break
    else:
        print('    value = {}'.format(line[line.find('=')+2:-1]))

print('    print(value)')
