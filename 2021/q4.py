from utils import *

with open('q4.txt') as file:
    file = file.read()

groups = split_strip(file, '\n\n')

nums = nats(groups[0])


def sol():
    boards = groups[1:]
    boards = [[nats(line) for line in lines(board)] for board in boards]

    done = [False] * len(board)

    for n in nums:
        for board in boards:
            for i, row in enumerate(board):
                for j, a in enumerate(row):
                    if a == n:
                        board[i][j] = -1
                        if all(a == -1 for a in row) or all(board[k][j] == -1 for k in range(len(board))):
                            return sum(a for row in board for a in row if a != -1) * n

print(sol())