from utils import *

with open('q18.txt') as file:
    file = file.read()

def add_p(p1, p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return (x1+x2, y1+y2, z1+z2)

adj = [(0,0,1),(0,1,0),(1,0,0),(0,0,-1),(0,-1,0),(-1,0,0)]

def neigh(p):
    return [add_p(p, a) for a in adj]

ps = set()

for line in lines(file):
    x,y,z = nats(line)
    ps.add((x,y,z))

# print(ps)

# p1 = tuple(nats(lines(file)[0]))

x_min = min(x for x,y,z in ps) - 1
x_max = max(x for x,y,z in ps) + 1
y_min = min(y for x,y,z in ps) - 1
y_max = max(y for x,y,z in ps) + 1
z_min = min(z for x,y,z in ps) - 1
z_max = max(z for x,y,z in ps) + 1

q = Queue()
done = set()
q.put((x_min, y_min, z_min))
done.add((x_min, y_min, z_min))

es = 0

while not q.empty():
    p = q.get()
    x,y,z = p
    for n in neigh(p):
        if n in ps:
            es += 1
        elif n not in done and x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max:
            done.add(n)
            q.put(n)

print(es)

s = 0

done = set()

for p1 in ps:
    if p1 in done:
        continue
    done.add(p1)
    q = Queue()
    q.put(p1)

    while not q.empty():
        p = q.get()
        for n in neigh(p):
            if n not in ps:
                s += 1
            elif n not in done:
                done.add(n)
                q.put(n)

print(s)