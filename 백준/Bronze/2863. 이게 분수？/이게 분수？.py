import sys
input = sys.stdin.readline


board = [list(map(int, input().split())) for _ in range(2)]


def rotate():
    temp = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            temp[j][2-i-1] = board[i][j]
    return temp


answer = 0
idx = -1
for i in range(4):
    result = board[0][0] / board[1][0] + board[0][1] / board[1][1]

    if answer < result:
        idx = i
        answer = result

    board = rotate()
print(idx)
