from utils import *

with open('q3.txt') as file:
    file = file.read()

freq = [Counter() for _ in range(12)]

for line in lines(file):
    for i, c in enumerate(line):
        freq[i][c] += 1

gamma = int("".join([counter.most_common()[0][0] for counter in freq]), base=2)
eps = int("".join([counter.most_common()[1][0] for counter in freq]), base=2)

print(gamma * eps)


nums = lines(file)

gamma = 0

for i in range(len(nums[0])):
    freq = Counter(num[i] for num in nums)
    bit = '1' if freq['1'] >= freq['0'] else '0'
    nums = [num for num in nums if num[i] == bit]
    if len(nums) == 1:
        gamma = int(nums[0], base=2)
        break

nums = lines(file)

eps = 0

for i in range(len(nums[0])):
    freq = Counter(num[i] for num in nums)
    bit = '0' if freq['0'] <= freq['1'] else '1'
    nums = [num for num in nums if num[i] == bit]
    if len(nums) == 1:
        eps = int(nums[0], base=2)
        break

print(gamma * eps)
