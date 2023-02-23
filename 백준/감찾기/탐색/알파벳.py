import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(input().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_length = 0


def bfs():
    queue = set()
    queue.add((0, 0, graph[0][0]))
    global max_length
    while queue:
        x, y, alpha = queue.pop()
        max_length = max(max_length, len(alpha))
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= r or my >= c:
                continue

            if graph[mx][my] in alpha:
                continue

            else:
                queue.add((mx, my, alpha+graph[mx][my]))


bfs()
print(max_length)
