# --- 요구 사항 ---
# 곰팡이들은 현재 여러 개의 덩어리를 이루고 있는 상태
# m행 n열. 한 칸 당 한 개의 곰팡이. 곰팡이의 덩어리 : 격자 상에 가로세로로 인접한 곰팡이들의 집합
# 맨 처음 상태에서는 한 덩어리 안의 곰팡이들이 모두 같은 종으로, 자라는 속도도 같다.
# 서로 다른 덩어리에 속한 곰팡이는 종이 달라 자라는 속도도 다를 수 있다.
#   시간이 지남에 따라 서로 다른 종의 곰팡이 덩어리가 한 덩어리로 합쳐지는 경우도 있을 수 있다.
#   만약 어느 곰팡이의 자라는 속도가 k라면, 하루가 지났을 때 그 곰팡이가 피어있던 자리를 중심으로 2k+1행 2k+1열의 격자에 같은 종의 곰팡이가 번진다는 의미이다.
#   만약 서로 다른 종의 곰팡이가 같은 칸에 번져 오면, 자라는 속도가 빠른 곰팡이가 그 칸을 차지한다.

# TODO: 곰팡이들이 점점 자라나서 한 덩어리로 될 때까지 시간?

# --- 풀이 방법 ---
# 1. 곰팡이들을 한번에 퍼뜨리기 위해 모든 곰팡이를 queue에 넣는다.
# 2. 자라는 속도가 빠른 곰팡이를 먼저 퍼뜨린다.
# 3. 곰팡이 중심으로 상하좌우 k만큼 격자를 자신으로 채운다.
# 4. k가 2라면, 곰팡이 중심으로 2만큼 떨어진 모든 격자를 채운다.
# FIXME: 한 번 퍼지는 건 성공했는데, 2번째 돌 때의 무한루프

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

board = [list(map(int, list(input().strip()))) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread():  # 자기를 중심으로 +- k만큼 격자를 채운다
    spread_board = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            speed = board[x][y]
            spread_board[x][y] = max(spread_board[x][y], board[x][y])
            if speed:
                for i in range(x-speed, x+speed+1):
                    for j in range(y-speed, y+speed+1):
                        if i < 0 or i >= n or j < 0 or j >= m:
                            continue

                        if board[i][j] < board[x][y]:
                            spread_board[i][j] = max(
                                spread_board[i][j], board[x][y])
    return spread_board


def bfs(x, y):  # 곰팡이 덩어리 탐색 bfs
    queue = deque([[x, y]])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if not visited[mx][my] and board[mx][my]:
                visited[mx][my] = 1
                queue.append([mx, my])


def check():  # 곰팡이 덩어리 개수 세는 함수
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                bfs(i, j)
                count += 1
    return count


answer = 0
visited = [[0]*m for _ in range(n)]
count = check()
while count > 1:
    visited = [[0]*m for _ in range(n)]
    board = spread()
    count = check()
    answer += 1
print(answer)
