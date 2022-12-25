from utils import *

with open('q25.txt') as file:
    file = file.read()

m = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
n = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}

total = 0

for line in lines(file):
    s = 0
    for c in line:
        s *= 5
        s += m[c]

    total += s

res = ''

pow = 1

print(total)

while total > 0:
    c = total % 5
    if c == 3:
        c = -2
    elif c == 4:
        c = -1

    res = n[c] + res

    total -= c
    total //= 5

print(res)