from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

maps = []
now_x, now_y = 0, 0
size = 2
for i in range(n):
    maps.append((list(map(int, input().split()))))
    for j in range(n):
        if maps[i][j] == 9:
            now_x, now_y = i, j
            maps[i][j] = 0


def bfs():
    distances = [[-1]*n for _ in range(n)]
    distances[now_x][now_y] = 0
    queue = deque()
    queue.append((now_x, now_y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if distances[mx][my] == -1 and maps[mx][my] <= size:
                distances[mx][my] = distances[x][y] + 1
                queue.append((mx, my))

    return distances


def find(dist):
    target_x, target_y = 0, 0
    INF = int(1e9)
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= maps[i][j] < size:
                if min_dist > dist[i][j]:
                    target_x, target_y = i, j
                    min_dist = dist[i][j]

    if min_dist == INF:
        return None
    else:
        return target_x, target_y, min_dist


answer = 0
count = 0
while True:
    result = find(bfs())
    if result == None:
        print(answer)
        break

    x, y, dist = result
    answer += dist
    now_x, now_y = x, y

    count += 1
    if count == size:
        size += 1
        count = 0
    maps[x][y] = 0
