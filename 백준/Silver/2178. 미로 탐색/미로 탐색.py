# NxM 2차원 배열.
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함.

# TODO: (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수?

# 1. n, m 입력받기
# 2. n, m 을 2차원 배열 만들기
# 3. bfs로 탐색하면서 거리 배열 만들기
# 4. visited[n-1][m-1] 출력

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []

visited = [[0]*m for _ in range(n)]

for _ in range(n):
    line = list(map(int, list(input().strip())))
    board.append(line)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([[x, y]])

    # 처음 위치도 칸에 포함한다.
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            # 방문하지 않았다 & 이동할 수 있다
            if not visited[mx][my] and board[mx][my] == 1:
                visited[mx][my] = visited[x][y] + 1
                queue.append([mx, my])


bfs(0, 0)
print(visited[n-1][m-1])
