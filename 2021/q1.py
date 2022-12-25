from utils import *

with open('q1.txt') as file:
    file = file.read()

a = nats(file)

print(sum(a[i+1] > a[i] for i in range(len(a) - 1)))

print(sum(sum(a[i+1:i+4]) > sum(a[i:i+3]) for i in range(len(a) - 3)))
