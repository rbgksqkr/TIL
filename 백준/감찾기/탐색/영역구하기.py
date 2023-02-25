import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
data = []
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if graph[i][j] == 0:
                graph[i][j] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = 1
    total = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if graph[mx][my] == 0 and visited[mx][my] == 0:
                visited[mx][my] = 1
                total += 1
                queue.append([mx, my])

    return total


visited = [[0 for _ in range(m)] for _ in range(n)]
result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == 0:
            result.append(bfs(i, j))

print(len(result))
result.sort()
for i in result:
    print(i, end=' ')
