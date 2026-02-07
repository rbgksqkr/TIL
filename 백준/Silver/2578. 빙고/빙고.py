import sys
input = sys.stdin.readline

board = []
for _ in range(5):
    line = list(map(int, input().split()))
    board.append(line)

numbers = []
for _ in range(5):
    line = list(map(int, input().split()))
    numbers.extend(line)

def bingo_count():
    count = 0

    # rows
    for r in range(5):
        if all(board[r][c] == -1 for c in range(5)):
            count += 1

    # cols
    for c in range(5):
        if all(board[r][c] == -1 for r in range(5)):
            count += 1

    # diagonal
    if all(board[i][i] == -1 for i in range(5)):
        count += 1

    # reverse diagonal
    if all(board[i][4 - i] == -1 for i in range(5)):
        count += 1

    return count

for idx, number in enumerate(numbers):
    count = 0
    flag = 0
    for i in range(5):
        if flag == 1:
            break
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = -1
                flag = 1
                break
    

    if bingo_count() >= 3:
        print(idx + 1)
        break