import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([[0, 0, 1]])
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while queue:
        x, y, wall = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if graph[mx][my] == 0 and visited[mx][my][wall] == 0:
                visited[mx][my][wall] = visited[x][y][wall] + 1
                queue.append([mx, my, wall])
            elif graph[mx][my] == 1 and wall == 1:
                visited[mx][my][0] = visited[x][y][1] + 1
                queue.append([mx, my, 0])

    return -1


print(bfs())