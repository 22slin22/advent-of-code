from utils import *

with open('q22.txt') as file:
    file = file.read()

m, intr_str = file.split('\n\n')
m = m.split('\n')

m = m
intr_str.strip()

instr = []

while len(intr_str) > 0:
    instr.append("".join(takewhile(lambda c: c.isdigit(), intr_str)))
    intr_str = "".join(dropwhile(lambda c: c.isdigit(), intr_str))

    if len(intr_str) == 0:
        break

    instr.append("".join(takewhile(lambda c: not c.isdigit(), intr_str)))
    intr_str = "".join(dropwhile(lambda c: not c.isdigit(), intr_str))

h, w = len(m), max(len(r) for r in m)

def in_bounds(x,y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    if x >= len(m[y]) or m[y][x] == ' ':
        return False
    return True

def walkable(x,y):
    return in_bounds(x,y) and m[y][x] == '.'

dirs = [(1,0), (0,1), (-1,0), (0,-1)]

def walk_until_walkable(x,y,dir):
    while not walkable(x,y):
        x += dir[0]
        y += dir[1]
    return x,y

y = 0
x = min(x for x in range(w) if walkable(x,0))
d = 0

def minus(x,y,dir):
    return (x-dir[0], y-dir[1])

def plus(x,y,dir):
    return (x+dir[0], y+dir[1])

print(instr)

def wrap(x,y,d):
    # print(x,y,d)
    if x < 0:
        if y < 150:     # 2L
            xn = 50
            yn = 149 - y
            dn = 0
        else:           # 1L
            yn = 0
            xn = 50 + y - 150
            dn = 1
            # print(xn,yn,dn)
    elif x < 50:
        if d == 3:      # 2U
            xn = 50
            yn = x + 50
            dn = 0   # R
        elif d == 1:    # 1D
            yn = 0
            xn = x + 100
            dn = 1   # D
        elif y < 50:    # 5L
            xn = 0
            yn = 149 - y
            dn = 0   # R
        else:           # 4L
            yn = 100
            xn = y - 50
            dn = 1  # D
    elif x < 100:
        if d == 0:      # 1R
            yn = 149
            xn = y - 100
            dn = 3  # U
        elif d == 1:    # 3D
            xn = 49
            yn = x + 100
            dn = 2   # L
        elif d == 3:    # 5U
            xn = 0
            yn = x + 100
            dn = 0  # R
    elif x < 150:
        if d == 1:      # 6D
            xn = 99
            yn = x - 50
            dn = 2  # L
        elif d == 3:    # 6U
            yn = 199
            xn = x - 100
            dn = 3  # U
        elif y < 100:   # 4R
            yn = 49
            xn = y + 50
            dn = 3  # U
        else:           # 3R    checked
            xn = 149
            yn = 149 - y
            dn = 2  # L
    else:               # 6R    checked
        xn = 99
        yn = 149 - y
        dn = 2  # L
        
    # print(xn,yn,dn)
    # print()
    return xn,yn,dn
        

for i in instr:
    # print(instr)
    if i == 'R':
        d = (d+1) % 4
    elif i == 'L':
        d = (d-1) % 4
    else:
        n = int(i)
        for k in range(n):
            nx, ny = plus(x,y,dirs[d])
            nd = d

            if not in_bounds(nx,ny):
                print(nx,ny,nd)
                nx,ny,nd = wrap(nx,ny,nd)
                print(nx,ny,nd)
                print()

                # nx,ny = minus(nx,ny,dirs[d])
                # while in_bounds(nx,ny):
                #     nx,ny = minus(nx,ny,dirs[d])
                # nx,ny = plus(nx,ny,dirs[d])

            if m[ny][nx] == '#':
                break
            x,y,d = nx,ny,nd

print(1000*(y+1) + 4*(x+1) + d)

