from utils import *

with open('q11.txt') as file:
    file = file.read()


mon = split_strip(file, '\n\n')

items = []
ops = []
test = []
true = []
false = []
n = [] 

for m in mon:
    ls = lines(m)
    items.append(nats(ls[1]))
    ops.append(str_after(' = ', ls[2]))
    test.append(first_nat(ls[3]))
    true.append(first_nat(ls[4]))
    false.append(first_nat(ls[5]))
    n.append(0)

mod = 1
for t in test:
    mod *= t

for r in range(10000):  # range(20) for part 1
    for m in range(len(items)):
        for item in items[m]:
            old = item
            # part 1:
            # new = eval(ops[m]) // 3 
            new = eval(ops[m]) % mod
            n[m] += 1
            if new % test[m] == 0:
                items[true[m]].append(new)
            else:
                items[false[m]].append(new)
        items[m] = []

n.sort()
print(n[-1] * n[-2])
