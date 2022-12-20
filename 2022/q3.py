from utils import *

with open("q3.txt") as file:
    p = lower_abc + upper_abc

    s = 0

    for line in file:
        a,b = line[:len(line)//2], line[len(line)//2:]

        for c in a:
            if c in b:
                s += p.index(c) + 1
                break

    print(s)
    

with open("q3.txt") as file:
    p = lower_abc + upper_abc

    s = 0

    lines = file.readlines()

    for i in range(len(lines)//3):
        a,b,c = lines[3*i],lines[3*i+1],lines[3*i+2]

        for x in a:
            if x in b and x in c:
                s += p.index(x) + 1
                break

    print(s)
    
