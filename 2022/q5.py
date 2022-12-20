from utils import *

'''
[Q]         [N]             [N]    
[H]     [B] [D]             [S] [M]
[C]     [Q] [J]         [V] [Q] [D]
[T]     [S] [Z] [F]     [J] [J] [W]
[N] [G] [T] [S] [V]     [B] [C] [C]
[S] [B] [R] [W] [D] [J] [Q] [R] [Q]
[V] [D] [W] [G] [P] [W] [N] [T] [S]
[B] [W] [F] [L] [M] [F] [L] [G] [J]
 1   2   3   4   5   6   7   8   9 
'''

c = [
    ['B','V','S','N','T','C','H','Q'],
    ['W','D','B','G'],
    ['F','W','R','T','S','Q','B'],
    ['L','G','W','S','Z','J','D','N'],
    ['M','P','D','V','F'],
    ['F','W','J'],
    ['L','N','Q','B','J','V'],
    ['G','T','R','C','J','Q','S','N'],
    ['J','S','Q','C','W','D','M']
]

with open("q5.txt") as file:
    for line in file:
        n, f, t = ints(line)
        f -= 1
        t -= 1

        for i in range(n):
            c[t].append(c[f][-n+i])
        for i in range(n):
            del c[f][-1]

    print("".join(a[-1] for a in c))