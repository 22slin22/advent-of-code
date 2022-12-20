from collections import defaultdict
from functools import cache

succ = defaultdict(list)
rate = {}

with open('q16.txt') as file:
    for line in file:
        words = line.split()
        v = words[1]
        rate[v] = int(words[4][5:-1])
        for u in words[9:]:
            succ[v].append(u.strip(','))

@cache
def solve(time, v, opened, others):
    if time == 0:
        return 0 if others == 0 else solve(26, 'AA', opened, others-1)

    flow = 0
    if v not in opened and rate[v] > 0:
        flow = rate[v] * (time-1) + max(flow, solve(time-1, v, tuple(sorted(list(opened) + [v])), others))
    for u in succ[v]:
        flow = max(flow, solve(time-1, u, opened, others))

    return flow

print(solve(30, 'AA', (), 0))   # Part 1
print(solve(26, 'AA', (), 1))   # Part 2