import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = []
min_height, max_height = 101, 0
for _ in range(n):
    line = list(map(int, input().split()))
    min_height = min(min_height, min(line))
    max_height = max(max_height, max(line))
    graph.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, graph):
    queue = deque([[x, y]])
    graph[x][y] = -1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if graph[mx][my] != -1:
                graph[mx][my] = -1
                queue.append([mx, my])


result = 1
for k in range(min_height, max_height+1):
    graph_copy = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph_copy[i][j] <= k:
                graph_copy[i][j] = -1
    count = 0
    for i in range(n):
        for j in range(n):
            if graph_copy[i][j] != -1:
                bfs(i, j, graph_copy)
                count += 1

    result = max(result, count)

print(result)
