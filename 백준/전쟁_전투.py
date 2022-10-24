from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for _ in range(m):
    data.append(list(input().strip()))

dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

visited = [[0]*n for _ in range(m)]

def bfs(x, y, team):
    global white, black
    queue = deque()
    queue.append((x, y))
    cnt = 1
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= m or my >= n:
                continue

            if visited[mx][my] == 0 and data[mx][my] == team:
                visited[mx][my] = 1
                cnt += 1
                queue.append((mx, my))

    if team == 'W':
        white += cnt**2
    else:
        black += cnt**2

# 가로 : 열(n), 세로 : 행(m)
white, black = 0, 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, data[i][j])

print(white, black)
