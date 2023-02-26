import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
now_x, now_y = 0, 0
now_size = 2
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 9:
            now_x, now_y = i, j
            line[j] = 0
    graph.append(line)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    distance[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if distance[mx][my] == -1 and graph[mx][my] <= now_size:
                distance[mx][my] = distance[x][y] + 1
                queue.append([mx, my])

    return distance


INF = int(1e9)


def find(distance):
    target_x, target_y = INF, INF
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 1 <= graph[i][j] < now_size:
                if min_dist > distance[i][j]:
                    min_dist = distance[i][j]
                    target_x, target_y = i, j

    if min_dist == INF:
        return 0
    else:
        return [target_x, target_y, min_dist]


result = 0
eating = 0
while True:
    target = find(bfs(now_x, now_y))
    if not target:
        break
    else:
        target_x, target_y, dist = target
        graph[target_x][target_y] = 0
        result += dist
        eating += 1
        now_x, now_y = target_x, target_y
        if now_size == eating:
            now_size += 1
            eating = 0

print(result)
