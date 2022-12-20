from utils import *
import functools

with open('q13.txt') as file:
    file = file.read()

groups = split_strip(file, '\n\n')


def parse(s: str):
    # print('Parsing', s)
    if s[0].isdigit():
        a = "".join(take_while(lambda c: c.isdigit(), s))
        return int(a), s[len(a):]
    else:
        s = s[1:]
        l = []
        while len(s) > 0 and s[0] != ']':
            x, s = parse(s)
            l.append(x)
            if s.startswith(','):
                s = s[1:]
        rest = '' if len(s) == 0 else s[1:]
        return l, rest

def compare(left, right):
    # print('Comparing', left, right)
    match left,right:
        case [], []:
            return 0
        case [], [*_]:
            return -1
        case [*_], []:
            return 1
        case [*l], [*r]:
            for i in range(len(l)):
                if i >= len(r):
                    return 1
                # if isinstance(l[i], int) and isinstance(r[i], int):
                #     if l[i] < r[i]:
                #         return True
                #     if l[i] > r[i]:
                #         return False
                elif compare(l[i], r[i]) != 0:
                    return compare(l[i], r[i])
            if len(l) < len(r):
                return -1
            return 0
        case [*left], right:
            return compare(left, [right])
        case left, [*right]:
            return compare([left], right)
        case left, right:
            return 1 if left > right else -1 if left < right else 0

n = 0

for i, group in enumerate(groups):
    # print(group)
    line1, line2 = lines(group)
    left, _ = parse(line1)
    right, _ = parse(line2)
    print(left)
    print(right)
    # if str(left).replace(' ', '') != line1:
    #     print(left, line1)
    # if str(right).replace(' ', '') != line2:
    #     print(right, line2)
    if compare(left, right) <= 0:
        print(i+1)
        n += i + 1

print(n)



packets = [line for line in lines(file) if len(line) != 0]
packets.append('[[2]]')
packets.append('[[6]]')

packets = [parse(p)[0] for p in packets]

div1 = packets[-2]
div2 = packets[-1]

packets.sort(key=functools.cmp_to_key(compare))

print((packets.index(div1)+1) * (packets.index(div2)+1))