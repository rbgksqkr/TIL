import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

target = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            target = [i, j]
    graph.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque([[i, j]])
    distance[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if 0 <= mx < n and 0 <= my < m and distance[mx][my] == -1 and graph[mx][my] == 1:
                distance[mx][my] = distance[x][y] + 1
                queue.append([mx, my])


distance = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
