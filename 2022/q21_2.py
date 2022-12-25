from utils import *

with open('q21.txt') as file:
    file = file.read()

succ = defaultdict(set)
pred = {}
number = {}
num_pred = {}
ops = {}

for line in lines(file):
    words = line.split()
    mon = words[0][:-1]
    if mon not in num_pred:
        num_pred[mon] = 0

    op = words[1:]
    new_op = []

    pred[mon] = set()
    for s in op:
        if s.isalpha():
            pred[mon].add(s)
            if mon not in succ[s]:
                succ[s].add(mon)
                new_op.append(s)
                num_pred[mon] += 1
        elif s == '/':
            new_op.append('//')
        else:
            new_op.append(s)
    ops[mon] = new_op

# print(ops['root'])
# print(ops['zhms'])

def solve(mon, target):
    while mon != 'humn':
        number[mon] = target
        print(mon, target)
        print(ops[mon])
        v1, op, v2 = ops[mon]
        print(v1 not in number, v2 not in number)
        match op:
            case '+':
                if v1 not in number and v2 not in number:
                    print('fuck')
                if v1 not in number:
                    v1,v2 = v2,v1
                print(v1, number[v1])
                mon = v2
                target = target - number[v1]
            case '-':
                if v1 not in number and v2 not in number:
                    print('fuck')
                if v1 not in number:
                    print(v2, number[v2])
                    mon = v1
                    target = target + number[v2]
                elif v2 not in number:
                    print(v1, number[v1])
                    mon = v2
                    target = number[v1] - target
                else:
                    print('fuck-')
            case '*':
                if v1 not in number and v2 not in number:
                    print('fuck')
                if v1 not in number:
                    v1,v2 = v2,v1
                print(v1, number[v1])
                mon = v2
                target = target // number[v1]
            case '//':
                if v1 not in number and v2 not in number:
                    print('fuck')
                if v1 not in number:
                    print(v2, number[v2])
                    mon = v1
                    target = target * number[v2]
                elif v2 not in number:
                    print(v1, number[v1])
                    mon = v2
                    target = number[v1] // target
                else:
                    print('fuck/')
                    break
                
    return target

q = Queue()

for m,n in num_pred.items():
    if n == 0:
        q.put(m)

while not q.empty():
    cur = q.get()

    if cur == 'humn':
        continue

    if cur == 'root':
        print(solve(ops[cur][0], number[ops[cur][2]]))
        break

    if len(ops[cur]) == 1:
        number[cur] = int(ops[cur][0])
    else:
        number[cur] = eval(f"{number[ops[cur][0]]} {ops[cur][1]} {number[ops[cur][2]]}")

    for s in succ[cur]:
        num_pred[s] -= 1
        if num_pred[s] == 0:
            q.put(s)


# number_mid = number
# num_pred_mid = num_pred

# print(max(num_pred.values()))

# for humn in range(10000000):
#     if humn % 1000 == 0:
#         print('iteration', humn)
    
#     q = Queue()
#     number = dict(number_mid)
#     num_pred = dict(num_pred_mid)

#     number['humn'] = humn

#     for s in succ['humn']:
#         q.put(s)

#     # for m,n in num_pred.items():
#     #     if n == 0:
#     #         q.put(m)

#     while not q.empty():
#         cur = q.get()

#         if cur == 'root':
#             # print(number[ops[cur][0]], number[ops[cur][2]])
#             if number[ops[cur][0]] == number[ops[cur][2]]:
#                 print(humn)
#                 exit()

#         if len(ops[cur]) == 1:
#             number[cur] = int(ops[cur][0])
#         else:
#             number[cur] = eval(f"{number[ops[cur][0]]} {ops[cur][1]} {number[ops[cur][2]]}")

#         for s in succ[cur]:
#             num_pred[s] -= 1
#             if num_pred[s] == 0:
#                 q.put(s)

# print()

print(solve(ops['root'][0], number[ops['root'][2]]))
