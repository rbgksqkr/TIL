# --- 요구 사항 ---
# 바이러스는 활성 상태와 비활성 상태가 있다.
# 가장 처음에 모든 바이러스는 비활성 상태이고,
# 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.
# 바이러스 M개를 활성 상태로 변경하려고 한다.
# N×N인 정사각형. 0은 빈 칸, 1은 벽, 2는 바이러스
# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
# TODO: 모든 빈 칸에 바이러스가 있게 되는 최소 시간 출력. 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우 -1 출력.

# --- 풀이 방법 ---
# 1. 바이러스의 활성 상태와 비활성 상태를 구분해서 저장.
# - 이전에는 바이러스가 있을 위치에도 퍼뜨렸는데 이번에는 새로운 바이러스로 만듦
# 2. 활성 바이러스 m개를 정한다.
# 3. 활성 바이러스가 인접한 칸으로 복제된다.
# 4. 최소 시간(count)을 퍼뜨리면서 계산한다.
# 5. 정해진 활성 바이러스로 bfs를 다 돈 후 빈칸이 있다면 INF 반환, 없으면 count 반환
# FIXME: 빈 칸만 방문하면 81%. 벽이 아닌 곳만 방문하면 86% 틀림

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)

board, virus = [], []

for i in range(n):
    line = list(map(int, input().split()))

    for j in range(n):
        if line[j] == 0:  # 빈 칸
            line[j] = -1
        if line[j] == 1:  # 벽
            line[j] = '-'
        if line[j] == 2:  # 비활성 바이러스
            virus.append([i, j])
            line[j] = 0
    board.append(line)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(data):
    visited = [[-1]*n for _ in range(n)]
    for x, y in data:
        visited[x][y] = 0
    queue = deque(data)
    count = 0  # 최소 거리

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            # 방문하지 않았고, 빈 칸일 때
            if visited[mx][my] == -1 and board[mx][my] == -1:
                visited[mx][my] = visited[x][y] + 1
                count = max(count, visited[x][y] + 1)  # 전체를 돌 때 걸린 최소 시간 저장
                queue.append([mx, my])

            # 방문하지 않았고, 비활성 바이러스일 때
            if visited[mx][my] == -1 and board[mx][my] == 0:
                visited[mx][my] = visited[x][y] + 1
                queue.append([mx, my])

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and board[i][j] == -1:  # 빈 칸인데 방문하지 않은 경우
                return INF
    return count


answer = INF
for data in list(combinations(virus, m)):
    answer = min(answer, bfs(data))
if answer == INF:
    print(-1)
else:
    print(answer)
