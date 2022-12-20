from utils import *
import functools

with open('q13.txt') as file:
    file = file.read()

def compare(left, right):
    match left,right:
        case [], []:
            return 0
        case [], [*_]:
            return -1
        case [*_], []:
            return 1
        case [l, *ls], [r, *rs]:
            cmp = compare(l, r)
            return cmp if cmp != 0 else compare(ls, rs)
        case [*left], right:
            return compare(left, [right])
        case left, [*right]:
            return compare([left], right)
        case left, right:
            return 1 if left > right else -1 if left < right else 0

n = 0
for i, group in enumerate(file.strip().split('\n\n')):
    left, right = map(eval, group.strip().split('\n'))
    if compare(left, right) <= 0:
        n += i + 1

print(n)


packets = [eval(line) for line in lines(file) if len(line) != 0] + [[[2]], [[6]]]
packets.sort(key=functools.cmp_to_key(compare))

print((packets.index([[2]])+1) * (packets.index([[6]])+1))