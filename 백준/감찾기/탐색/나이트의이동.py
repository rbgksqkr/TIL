import sys
from collections import deque
input = sys.stdin.readline

move = [(-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)]


def bfs(x, y):
    queue = deque([[x, y]])
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            mx = x + move[i][0]
            my = y + move[i][1]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if graph[mx][my] > graph[x][y] + 1:
                graph[mx][my] = graph[x][y] + 1
                queue.append([mx, my])


T = int(input())

for _ in range(T):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    INF = int(1e9)
    graph = [[INF for _ in range(n)] for _ in range(n)]
    bfs(start[0], start[1])
    print(graph[end[0]][end[1]])
