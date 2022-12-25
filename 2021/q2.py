from utils import *

with open('q2.txt') as file:
    file = file.read()

dirs = {'forward': V.RIGHT(), 'up': V.UP(), 'down': V.DOWN()}

s = V(0,0)

for line in lines(file):
    d, n = line.split()
    s += dirs[d] * int(n)

print(s.x * s.y)

h = 0
depth = 0
aim = 0
for line in lines(file):
    d, n = line.split()
    n = int(n)

    match d:
        case 'down':
            aim += n
        case 'up':
            aim -= n
        case 'forward':
            h += n
            depth += aim * n

print(h * depth)