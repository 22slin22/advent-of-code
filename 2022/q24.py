from utils import *

with open('q24.txt') as file:
    file = file.read()

bls = defaultdict(list)

dirs = {'^': V.UP(), '<': V.LEFT(), '>': V.RIGHT(), 'v': V.DOWN()}

for y, line in enumerate(lines(file)):
    for x, c in enumerate(line):
        if c in '^<>v':
            bls[V(x,y)].append(dirs[c])

bls_start = bls

h = len(lines(file))
w = len(lines(file)[0])

step = 0

entry = V(1,0)

g = V(w-2,h-1)

def advance_bls():
    global bls
    global step

    new_bls = defaultdict(list)
    for q,bs in bls.items():
        for b in bs:
            xn,yn = q + b
            if xn == 0:
                xn = w - 2
            if xn == w - 1:
                xn = 1
            if yn == 0:
                yn = h - 2
            if yn == h - 1:
                yn = 1
            new_bls[V(xn,yn)].append(b)
    bls = new_bls
    step += 1

def succ(s):
    stp, p = s
    if step == stp:
        advance_bls()
    
    return [(stp + 1, n) for n in p.neigh_straight() + [p] if (n == entry or n == g or V(0,0) < n < V(w-1,h-1)) and len(bls[n]) == 0]

print(len(bfs_find((0, entry), succ, goal=lambda s: s[1] == g)) - 1)

def succ2(s):
    stp, to_goal, to_start, p = s
    if step == stp:
        advance_bls()
    
    return [(stp + 1,to_goal or n == g, to_start or (to_goal and n == entry), n) for n in p.neigh_straight() + [p] if (n == entry or n == g or V(0,0) < n < V(w-1,h-1)) and len(bls[n]) == 0]

bls = bls_start
step = 0

print(len(bfs_find((0, False, False, entry), succ2, goal=lambda s: s[3] == g and s[1] and s[2])) - 1)
