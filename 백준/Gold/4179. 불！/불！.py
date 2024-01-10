from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

board = []
queue_j = deque()
queue_f = deque()
dist_j = [[-1 for _ in range(c)] for _ in range(r)]
dist_f = [[-1 for _ in range(c)] for _ in range(r)]
for i in range(r):
    line = list(input().strip())
    for j in range(c):
        if line[j] == 'J':
            start = [i, j]
            dist_j[i][j] = 0
            queue_j.append([i, j, 0])
        elif line[j] == 'F':
            dist_f[i][j] = 0
            queue_f.append([i, j, 0])
    board.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = -1
while queue_f:
    x, y, count = queue_f.popleft()

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or my < 0 or mx >= r or my >= c:
            continue

        if dist_f[mx][my] >= 0 or board[mx][my] == '#':
            continue

        dist_f[mx][my] = dist_f[x][y] + 1
        queue_f.append([mx, my, count+1])

while queue_j:
    x, y, count = queue_j.popleft()

    if x == 0 or y == 0 or x == r - 1 or y == c - 1:
        result = dist_j[x][y] + 1
        break

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or my < 0 or mx >= r or my >= c:
            break

        if dist_f[mx][my] != -1 and dist_j[x][y] + 1 >= dist_f[mx][my]:
            continue

        if board[mx][my] == '#' or dist_j[mx][my] >= 0:
            continue

        dist_j[mx][my] = dist_j[x][y] + 1
        queue_j.append([mx, my, count+1])

if result == -1:
    print('IMPOSSIBLE')
else:
    print(result)
