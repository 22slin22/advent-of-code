from utils import *

with open("q8.txt") as file:
    g = Grid(map(int, line) for line in lines(file.read()))

    print(sum( any(all(g[r] < g[p] for r in ray) for ray in g.rays(p)) for p in g.points))

    def score(p):
        return prod(len(take_while(lambda r: g[r] < g[p], ray, True)) for ray in g.rays(p))

    print(max(score(p) for p in g.points))
