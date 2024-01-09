import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())  # 가로, 세로

graph = []
tomato = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 1:
            tomato.append([i, j])
    graph.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([])
    global day
    for x, y in tomato:
        queue.append([x, y, 0])
    while queue:
        x, y, count = queue.popleft()
        day = max(day, count)
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if graph[mx][my] == 0:
                graph[mx][my] = 1
                queue.append([mx, my, count + 1])


day = 0
bfs()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            day = -1
print(day)