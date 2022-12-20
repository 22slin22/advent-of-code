from utils import *

with open('q18.txt') as file:
    ps = [V3(*nats(coords)) for coords in file]

x_min = min(x for x,y,z in ps) - 1
x_max = max(x for x,y,z in ps) + 1
y_min = min(y for x,y,z in ps) - 1
y_max = max(y for x,y,z in ps) + 1
z_min = min(z for x,y,z in ps) - 1
z_max = max(z for x,y,z in ps) + 1

p_min = V3(x_min,y_min,z_min)
p_max = V3(x_max,y_max,z_max)

s = 0

for x in range(x_min, x_max + 1):
    for y in range(y_min, y_max + 1):
        for z in range(z_min, z_max + 1):
            p = V3(x,y,z)
            s += sum(n in ps for n in p.neigh_straight())

print(s)

es = 0

def succ(p):
    return [n for n in p.neigh_straight() if p_min <= n <= p_max]

def do(p):
    global es
    es += sum(n in ps for n in p.neigh_straight())

bfs(p_min, succ, do)

print(es)