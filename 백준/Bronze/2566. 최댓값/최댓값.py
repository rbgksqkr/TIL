import sys
input = sys.stdin.readline


array = [list(map(int, input().split())) for _ in range(9)]

answer = []
max_value = 0
for i in range(9):
    for j in range(9):
        if max_value <= array[i][j]:
            max_value = array[i][j]
            answer = [i, j]
row, col = answer
print(max_value)
print(row+1, col+1)
