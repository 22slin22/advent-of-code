from utils import *

with open("q1.txt") as file:
    elves = [sum(ints(elf)) for elf in split_strip(file.read(), '\n\n')]

print(max(elves))
print(sum(top(3, elves)))
