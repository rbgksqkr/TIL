import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())

graph = [[] for _ in range(h)]
tomato = []
for k in range(h):
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j] == 1:
                tomato.append([k, i, j, 0])
        graph[k].append(line)

# 상, 하, 좌, 우, 위, 아래
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]


def bfs():
    queue = deque(tomato)
    result = 0
    while queue:
        z, x, y, count = queue.popleft()
        result = max(result, count)
        for i in range(6):
            mx = x + dx[i]
            my = y + dy[i]
            mz = z + dz[i]

            if mx < 0 or my < 0 or mz < 0 or mx >= n or my >= m or mz >= h:
                continue

            if graph[mz][mx][my] == 0:
                graph[mz][mx][my] = 1
                queue.append([mz, mx, my, count+1])
    return result


answer = bfs()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                answer = -1

print(answer)
