import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([[x, y]])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if graph[mx][my] == 1 and visited[mx][my] == 0:
                visited[mx][my] = 1
                queue.append([mx, my])


T = int(input())
for _ in range(T):
    n, m, v = map(int, input().split())  # 가로, 세로, 배추개수
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(v):
        a, b = map(int, input().split())
        graph[a][b] = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
