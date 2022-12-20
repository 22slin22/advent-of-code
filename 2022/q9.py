from utils import *

with open('q9.txt') as file:
    file = file.read()


pos = set()
rope = [V(0,0) for i in range(10)]

dirs = {'U': V.UP(), 'L': V.LEFT(), 'R': V.RIGHT(), 'D': V.DOWN()}

for line in lines(file):
    d, n = line.split()
    n = int(n)

    i = 0

    for _ in range(n):
        if i > 10: break
        rope[0] += dirs[d]
        for i in range(1, len(rope)):
            if rope[i] not in rope[i-1].neigh9():
                if rope[i].x == rope[i-1].x or rope[i].y == rope[i-1].y:
                    rope[i] = [p for p in rope[i].neigh_straight() if p in rope[i-1].neigh_straight()][0]
                else:
                    rope[i] = [p for p in rope[i].neigh_diag() if p in rope[i-1].neigh8()][0]
            pos.add(rope[-1])

print(len(pos))
