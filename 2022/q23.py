from utils import *

with open('q23.txt') as file:
    file = file.read()

els : set[V] = set()

for y, line in enumerate(lines(file)):
    for x, c in enumerate(line):
        if c == '#':
            els.add(V(x,y))

dirs = [V.UP(), V.DOWN(), V.LEFT(), V.RIGHT()]

def check(p, d: V):
    if d == V.UP():
        return [V.UR(), V.UP(), V.UL()]
    elif d == V.DOWN():
        return [V.DL(), V.DOWN(), V.DR()]
    elif d == V.LEFT():
        return [V.UL(), V.LEFT(), V.DL()]
    elif d == V.RIGHT():
        return [V.UR(), V.RIGHT(), V.DR()]
    else:
        print('FUCK')

def p(rx,ry):
    for y in ry:
        for x in rx:
            if V(x,y) in els:
                print('#',end='')
            else:
                print('.',end='')
        print()
    print()

p(range(-4,10), range(-4,10))

n = 1
for _ in range(100000):
    prop = {}
    dup = set()
    for e in els:
        if all(n not in els for n in e.neigh8()):
            prop[e] = e
        else:
            for d in dirs:
                if all(e + n not in els for n in check(e, d)):
                    if e + d in prop.values():
                        dup.add(e+d)
                    prop[e] = e + d
                    break
            else:
                prop[e] = e
    
    els_new = {p if p not in dup else e for e,p in prop.items()}

    if els_new == els:
        print(n)
        break

    els = els_new

    dirs = dirs[1:] + [dirs[0]]

    # p(range(-4,10), range(-4,10))

    n += 1

print( (max(x for x,y in els) - min(x for x,y in els) + 1) * (max(y for x,y in els) - min(y for x,y in els) + 1) - len(els))