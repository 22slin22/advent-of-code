from utils import *

with open('q12.txt') as file:
    file = file.read()

g = Grid([[0 if c == 'S' else 25 if c == 'E' else lower_abc.index(c) for c in line] for line in lines(file)])

e, s = None, None

for i, row in enumerate(lines(file)):
    if 'S' in row:
        s = V(row.index('S'), i)
    if 'E' in row:
        e = V(row.index('E'), i)

print(len(bfs(s, lambda p: [q for q in g.neigh_straight_of(p) if g[q] <= g[p] + 1], e)) - 1)

print(len(bfs(e, lambda p: [q for q in g.neigh_straight_of(p) if g[q] >= g[p] - 1], lambda p: g[p] == 0)) - 1)