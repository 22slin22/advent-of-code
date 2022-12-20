from utils import *
from timeit import timeit

def solve():
    with open('q15.txt') as file:
        file = file.read()

    ss = {}
    bs = []

    def dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    for line in lines(file):
        sx, sy, bx, by = ints(line, seps=' =,:')
        ss[(sx,sy)] = dist((sx,sy),(bx,by))
        bs.append((bx,by))

    y = 2000000

    ranges = set()

    for s, d in ss.items():
        r = set(range(s[0] - (d - abs(s[1] - y)), s[0] + (d - abs(s[1] - y)) + 1))
        ranges |= r
            
    ranges -= set(bx for (bx,by) in bs if by == y)

    print(len(ranges))

    def find():
        todo = [(0,4000000,0,4000000)]
        
        while len(todo) != 0:
            x1,x2,y1,y2 = todo[-1]
            del todo[-1]

            for s,d in ss.items():
                if all(dist(p, s) <= d for p in [(x1,y1), (x1,y2), (x2,y1), (x2,y2)]):
                    break
            else:
                if x1 == x2 and y1 == y2:
                    return x1 * 4000000 + y1
                else:
                    xmid = (x1 + x2) // 2
                    ymid = (y1 + y2) // 2
                    for a,b,c,d in [(x1,xmid, y1, ymid), (x1, xmid, ymid+1, y2), (xmid+1,x2,y1,ymid), (xmid+1,x2,ymid+1,y2)]:
                        todo.append((a,b,c,d))

    print(find())


print(timeit(solve, number=20))