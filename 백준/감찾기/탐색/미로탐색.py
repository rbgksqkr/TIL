import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if graph[mx][my] == 1 and visited[mx][my] == 0:
                visited[mx][my] = 1
                graph[mx][my] = graph[x][y] + 1
                queue.append((mx, my))


bfs(0, 0)
print(graph[n-1][m-1])
