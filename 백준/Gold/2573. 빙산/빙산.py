# --- 요구 사항 ---
# 빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장
# 빙산 이외의 바다에 해당되는 칸에는 0이 저장
# 산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
# 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
# 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력
# TODO: 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)

# --- 풀이 방법 ---
# 1. 빙산에서 동서남북에 0의 개수만큼 높이 줄이기
# 2. 모든 빙산의 높이를 줄이고, 한 턴이 돌 때마다 시간(년) += 1
# 3. 한 턴이 돌 때마다 빙산이 붙어있는지 확인 : 2차원 배열 전체를 돌아 빙산일 때 dfs 돌기
# 빙산의 높이를 줄이면 다른 탐색에 영향을 준다. 한 번 돌 때 한번에 반영하려면 어떻게 하는가?
# - 모든 것을 한번에 하지 않기. 한 턴에 대한 탐색만 진행하고, 해당 인덱스 + 얼마나 높이를 줄일 지에 대한 정보를 배열로 반환

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
boards = []
for i in range(n):
    boards.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def countWater(x, y):
    count = 0
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if boards[mx][my] == 0:
            count += 1
    return count


def decreaseHeight(data):
    for i in data:
        x, y, count = i
        boards[x][y] -= count
        boards[x][y] = max(boards[x][y], 0)


def bfs(i, j):
    result = []
    queue = deque([[i, j]])
    visited[i][j] = 1
    result.append([i, j, countWater(i, j)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if boards[mx][my] != 0 and not visited[mx][my]:
                visited[mx][my] = 1
                queue.append([mx, my])
                result.append([mx, my, countWater(mx, my)])
    return result


answer = 0  # 시간(년)
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    result = []  # [높이를 내릴 빙산 x, y, 내려갈 높이]
    iceCount = 0
    for i in range(n):
        for j in range(m):
            if boards[i][j] != 0 and not visited[i][j]:
                result = bfs(i, j)
                iceCount += 1

    if iceCount == 0:
        answer = 0
        break

    if iceCount > 1:  # 다 녹거나 두 덩어리로 분리될 경우
        break

    decreaseHeight(result)  # 높이 한번에 내리기

    answer += 1

print(answer)
