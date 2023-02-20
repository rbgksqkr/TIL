import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if graph[mx][my] == 1 and not visited[mx][my]:
                visited[mx][my] = 1
                queue.append([mx, my])


while True:
    m, n = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    if n == 0 and m == 0:
        break

    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)
