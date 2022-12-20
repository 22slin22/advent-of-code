from utils import *

with open("q4.txt") as file:
    file = file.read()

s = 0

for line in lines(file):
    a,b,c,d = nats(line)

    if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d:
        s += 1

print(s)
