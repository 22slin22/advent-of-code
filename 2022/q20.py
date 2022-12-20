from utils import *

with (open('q20.txt')) as file:
    ns = ints(file.read())

ns_sorted = list(ns)

m = len(ns)

indices = list(range(m))

print(m)

print(len(set(ns)))

ns = [n * 811589153 for n in ns]

for _ in range(10):
    for n in range(m):
        i = indices.index(n)
        val = ns[n]
        # for j in range(abs(n)):
        #     if n < 0:
        #         ns[(i-j-1) % m], ns[(i-j) % m] = ns[(i-j) %m], ns[(i-j-1) %m]
        #         if ns[0] == n:
        #             del ns[0]
        #             ns.append(n)
        #     else:
        #         ns[(i+j+1) % m], ns[(i+j) % m] = ns[(i+j) % m], ns[(i+j+1) % m]
        #         if ns[-1] == n:
        #             del ns[-1]
        #             ns.in

        # if n < 0:
        #     i_new = (i+n-1)%(m-1) + 1
        # else:
        #     i_new = (i+n)%(m-1)

        if val < 0:
            after = (i+val-1)%(m-1)
            del indices[i]
            indices.insert(after+1,n)
            # print(f"Moved {n} from {i} to {after+1}")
        elif val >= 0:
            before = (i+val)%(m-1)
            del indices[i]
            indices.insert(before, n)
            # print(f"Moved {n} from {i} to {before}")
        else:
            continue

        # print("Moving", n)
        # print(ns)

i = indices.index(ns.index(0))

print(ns[indices[(i+1000)%m]] + ns[indices[(i+2000)%m]] + ns[indices[(i+3000)%m]])