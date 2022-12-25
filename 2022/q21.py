from utils import *

with open('q21.txt') as file:
    file = file.read()

succ = defaultdict(set)
num_pred_start = {}
ops = {}

for line in lines(file):
    words = line.split()
    mon = words[0][:-1]
    if mon not in num_pred_start:
        num_pred_start[mon] = 0

    op = words[1:]
    new_op = []
    for s in op:
        if s.isalpha() and mon not in succ[s]:
            succ[s].add(mon)
            new_op.append(f"number['{s}']")
            num_pred_start[mon] += 1
        elif s == '/':
            new_op.append('//')
        else:
            new_op.append(s)
    ops[mon] = " ".join(new_op)


num_pred_start['humn'] = 0

for humn in range(1000000000):

    num_pred = dict(num_pred_start)

    number = {}
    number['humn'] = humn

    q = Queue()

    for m,n in num_pred.items():
        if n == 0:
            q.put(m)

    while not q.empty():
        cur = q.get()
        if cur == 'root':
            w = ops[cur].split()
            v1,v2 = eval(w[0]), eval(w[2])
            # print(v1, v2)
            if v1 == v2:
                print(humn)
            break
        elif cur == 'humn':
            pass
        else:
            # print(cur)
            # print(num_pred[cur])
            # print(ops[cur])
            number[cur] = eval(ops[cur])

        for s in succ[cur]:
            num_pred[s] -= 1
            if num_pred[s] == 0:
                q.put(s)