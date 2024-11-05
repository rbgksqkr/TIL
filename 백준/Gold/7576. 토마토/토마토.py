# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# TODO: 창고에 보관된 토마토들이 다 익게 되는 최소 일수?
# FIXME: 지도가 변경되는 경우 토마토의 좌표를 미리 저장해야 되는가?

# 1. 가로(m), 세로(n) 입력받기
# 2. 토마토들의 정보 2차원 배열에 저장
# 3. 토마토들을 배열에 저장
# 4. 현재 상태에서의 토마토 퍼지고, 시간을 거리로 저장해도 될듯

# 토마토가 모두 익을 때까지의 최소 날짜 출력
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0 출력
# 토마토가 모두 익지는 못하는 상황이면 -1 출력

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = []
queue = deque()


for i in range(n):
    line = list(map(int, input().split()))

    for j in range(m):
        if line[j] == 1:
            queue.append([i, j])

    board.append(line)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if board[mx][my] == 0:
                board[mx][my] = board[x][y] + 1
                queue.append([mx, my])


bfs()


max_value = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit()

    max_value = max(max_value, max(board[i]))
print(max_value-1)
