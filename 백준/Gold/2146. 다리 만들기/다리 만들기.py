# --- 요구사항 ---
# N×N크기의 이차원 평면상에 존재
# 섬이란 동서남북으로 육지가 붙어있는 덩어리
# 한 섬과 다른 섬을 잇는 다리 하나만을 만들기
# 다리를 가장 짧게 하여 최소 비용
# 가장 짧은 다리 : 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리
# TODO: 지도가 주어질 때, 두 대륙을 연결하는 다리의 최소 거리?

# --- 요구사항 ---
# 1. 바다와 접하는 부분을 모두 queue에 넣기
# 2. bfs로 가장 먼저 다른 대륙에 닿을 경우 거리 계산
# 3. queue에 넣을 때 count를 추가하여 다리 길이 계산
# 4. 1-2번 섬 연결보다 2-3번 섬 연결이 더 짧을 수 있으므로 모든 섬을 다 돌아아함

import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())
boards = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, idx):
    island = []

    visited[x][y] = idx

    queue = deque([[x, y]])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if visited[mx][my] == 0:
                if boards[mx][my] == 1:
                    visited[mx][my] = idx
                    queue.append([mx, my])
                elif boards[mx][my] == 0:
                    island.append([x, y])
    return island


def connectBridge(data, visited):
    global answer
    queue = deque(data)
    visited = copy.deepcopy(visited)

    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if visited[mx][my] == 0:
                visited[mx][my] = visited[x][y]
                queue.append([mx, my, count+1])
            elif visited[mx][my] != visited[x][y]:  # 육지인데 나랑 다른 육지
                answer = min(answer, count)
                return


idx = 1
visited = [[0 for _ in range(n)] for _ in range(n)]
saved_islands = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and boards[i][j] == 1:
            saved_islands.append(bfs(i, j, idx))
            idx += 1

answer = int(1e9)
for island in saved_islands:
    unique_list = list(set(map(tuple, island)))
    coords = list(map(list, unique_list))
    for i in range(len(coords)):
        coords[i] = coords[i] + [0]
    connectBridge(coords, visited)

print(answer)
