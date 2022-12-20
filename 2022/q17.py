from utils import *

with open('q17.txt') as file:
    file = file.read().strip()

rocks = {}

rs = [
    [[True, True, True, True]],
    [[False, True, False],
    [True, True, True],
    [False, True, False]],
    [[False, False, True],
    [False, False, True],
    [True, True, True]],
    [[True],[True],[True],[True]],
    [[True, True],
    [True, True]]
]

cave = set()

def in_bounds(rock, x, y):
    for i, row in enumerate(rock):
        for j, c in enumerate(row):
            if c:
                if x+j < 0 or x+j >= 7 or y-i < 0 or (x+j,y-i) in cave:
                    return False
    return True

# y_max = 0

def print_cave(y):
    for y in range(y,-1,-1):
        for x in range(7):
            if (x,y) in cave:
                print("#",end='')
            else:
                print('.', end='')
        print('')
    print('')

seen = [{} for _ in file]

s = 0
t = 0

y_plus = 0

skipped = False

while t < 1000000000000:
    if t % 1000 == 0:
        print(t)

    if not skipped and t % 5 == 3 and t > 5:
        y_max = max(y for _,y in cave)
        top_five = tuple([tuple([(x,y) in cave for x in range(7)]) for y in range(y_max-300, y_max+1)])
        if (top_five, t % 5) in seen[s]:
            n,h = seen[s][(top_five, t % 5)]
            skipping = (1000000000000 - t) // (t-n)
            y_plus += (y_max - h) * skipping
            print("skipping", skipping, "n:", n,'h:', h, 't:',t, 'y_max:', y_max)
            # print(top_five)
            t += skipping * (t-n)
            skipped = True
            if t >= 1000000000000:
                print('fuck', t)
                break
        else:
            seen[s][(top_five, t % 5)] = (t,y_max)
            # print("seen new")

    rock = rs[t % 5]
    x = 2
    y = 3 if len(cave) == 0 else max(y for _,y in cave) + 3 + len(rock)

    # print(x, y)

    # print('new rock')
    while True:
        if file[s % len(file)] == '<':
            if in_bounds(rock, x-1, y):
                # print('move left')
                x -= 1
        else:
            if in_bounds(rock, x+1, y):
                # print('move right')
                x += 1
        s += 1
        if s >= len(file):
            s = 0
        if in_bounds(rock, x, y-1):
            # print('move down')
            y -= 1
        else:
            for i, row in enumerate(rock):
                for j, c in enumerate(row):
                    if c:
                        cave.add((x+j,y-i))
            break

    y_max = max(y for _,y in cave)
    remove = [(x,y) for (x,y) in cave if y + 300 < y_max]
    for r in remove:
        cave.remove(r)

    t += 1
    # print_cave(10)

print(max(y for _,y in cave) + 1 + y_plus, y_plus)