# --- 요구 사항 ---
# 특정 위치에 바이러스 M개 배치, 승원이의 신호와 동시에 바이러스는 퍼지게 된다.
# 연구소는 크기가 N×N인 정사각형. 빈 칸(0), 벽(1), 바이러스를 놓을 수 있는 칸(2)으로 이뤄짐.
# 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.
# TODO: 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간? 퍼뜨릴 수 없는 경우 -1 출력.

# --- 풀이 방법 ---
# 1. 바이러스를 놓을 수 있는 칸(2) 중 M개를 선택해서 배치한다.
# 2. 모든 바이러스를 한번에 큐에 넣고 한번에 bfs를 돌린다. (1초에 한번 움직이기 위해)
# 3. 방문할 때 dist[mx][my] = dist[x][y] + 1 로 경로 표현하기.
# 3. bfs가 끝난 후 min값을 찾고, 빈 칸이 있는 경우 -1 출력하기
# FIXME: 82% 틀림.

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)

board = []
virus = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 0:
            line[j] = -1  # 빈 칸
        if line[j] == 1:
            line[j] = '-'  # 벽
        if line[j] == 2:
            virus.append([i, j])
            line[j] = 0  # 바이러스 빈 칸
    board.append(line)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(data):
    queue = deque(data)
    count = 0
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for x, y in data:
        visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if visited[mx][my] == -1 and (board[mx][my] == -1 or board[mx][my] == 0):
                visited[mx][my] = visited[x][y] + 1
                count = max(count, visited[x][y] + 1)
                queue.append([mx, my])

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and (board[i][j] == -1 or board[i][j] == 0):
                return INF
    return count


answer = INF
for data in list(combinations(virus, m)):
    selected_list = list(data)
    answer = min(answer, bfs(selected_list))

if answer == INF:
    print(-1)
else:
    print(answer)
