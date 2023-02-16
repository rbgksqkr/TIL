import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(n)] for _ in range(n)]


def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = 1
    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if graph[mx][my] == 1 and visited[mx][my] == 0:
                visited[mx][my] = 1
                count += 1
                queue.append([mx, my])

    return count


space = []
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            space.append(bfs(i, j))

space.sort()
print(len(space))
for i in space:
    print(i)
