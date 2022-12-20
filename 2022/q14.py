from utils import *

with open('q14.txt') as file:
    file = file.read()

cave = [[False] * 1000 for _ in range(500)]

y_max = 0

for line in lines(file):
    ps = line.split(' -> ')
    ps = list(map(nats, ps))

    for i in range(len(ps) - 1):
        y_max = max(y_max, ps[i][1])
        y_max = max(y_max, ps[i+1][1])
        for x in range(min(ps[i][0], ps[i+1][0]), max(ps[i][0], ps[i+1][0]) + 1):
            for y in range(min(ps[i][1], ps[i+1][1]), max(ps[i][1], ps[i+1][1]) + 1):
                cave[y][x] = True

for x in range(1000):
    cave[y_max+2][x] = True

def solve():
    n = 0
    while True:
        if cave[0][500]:
            return n
        s = [500, 0]

        while s[1] < 499:
            if not cave[s[1] + 1][s[0]]:
                s[1] += 1
            elif not cave[s[1] + 1][s[0] - 1]:
                s[1] += 1
                s[0] -= 1
            elif not cave[s[1] + 1][s[0] + 1]:
                s[1] += 1
                s[0] += 1
            else:
                cave[s[1]][s[0]] = True
                n += 1
                break
        else:
            return n

n = solve()
print(n)
