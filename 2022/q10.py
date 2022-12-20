from utils import *

with open("q10.txt") as file:
    file = file.read()

ops = []
for line in lines(file):
    if line == 'noop':
        ops.append(0)
    else:
        ops.append(0)
        ops.append(ints(line)[0])


i = 1
x = 1

s = 0

while i <= 240:
    if (i-20) % 40 == 0:
        s += i * x
    if abs(((i-1) % 40) - x) <= 1:
        print("#", end='')
    else:
        print(".", end='')
    if i % 40 == 0:
        print('')
    x += ops[i-1]
    i += 1

print(s) 