from collections import deque
import copy
from itertools import combinations
n, m = map(int, input().split())

maps = []
virus = []
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j] == 2:
            virus.append((i, j))


def makeWall():
    spaces = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                spaces.append((i, j))

    max_count = 0
    for space in list(combinations(spaces, 3)):
        temp_map = copy.deepcopy(maps)
        for x, y in space:
            temp_map[x][y] = 1
        spread(temp_map)
        max_count = max(max_count, getScore(temp_map))
        for x, y in space:
            temp_map[x][y] = 0
    print(max_count)


def spread(temp_map):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque(virus)
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if temp_map[mx][my] == 0:
                temp_map[mx][my] = 2
                queue.append((mx, my))


def getScore(temp_map):
    count = 0
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                count += 1
    return count


makeWall()
