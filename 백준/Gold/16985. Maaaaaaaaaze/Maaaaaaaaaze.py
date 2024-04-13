# -- 요구사항 ---
# 5×5 크기의 판이 5개
# 주어진 판들을 회전 가능
# 판을 쌓는 순서 자유
# 입구 : 정육면체에서 참가자가 임의로 선택한 꼭짓점에 위치한 칸
# 출구 : 입구와 면을 공유하지 않는 꼭짓점에 위치한 칸
#  -> 입구와 출구는 대각선 정반대
# TODO: 가장 적은 이동 횟수? 모든 경우에 탈출을 못하면 -1 출력

# --- 풀이 방법 ---
# 1. 판 결정 (4방향 회전 고려 : 4)
# 2. 쌓는 순서 결정 (5개의 판 순서 결정 : 5! = 120)
# 3. 입구, 출구 결정 (4개의 꼭짓점 순회 : 4)
# 4. 탐색 (5 * 5 * 5 = 125)

# 판이 결정된 상태에서 임의의 입구, 출구 결정해서 탐색로직부터 짜기 (O)
# 판 돌리는 함수 구현 (O)
# 각각의 판을 돌린 후 탐색 (O)
# 쌓는 순서 결정 (O)

# --- 힌트 ---
# 모든 판을 돌리고 순서도 바꾸니까 입구 출구를 [0, 0, 0], [4, 4, 4] 로 고정해도 됨
# 1~5층 회전(4^5) * 쌓는 순서(5! = 120) * 탐색(5^3 = 125) = 10^7 = 백만
# --- 시간초과 ---
# 최단 거리(12)인 경우 프로그램 종료
# BFS의 경우 도착점에 제일 먼저 도착한 경우가 최솟값이므로 도착점에서 탐색 종료

import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

# boards 원본 3차원 배열 저장
boards = []
for _ in range(5):
    board = [list(map(int, input().split())) for _ in range(5)]
    boards.append(board)
copy_boards = [[[0 for _ in range(5)] for _ in range(5)]
               for _ in range(5)]  # 돌린 상태의 boards
orders = list(permutations([0, 1, 2, 3, 4], 5))


def rotate_clockwise(board):  # 2차원 배열 시계방향  회전
    temp = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[j][4-i] = board[i][j]
    return temp


# 탐색 방향 : 상, 하, 좌, 우, 위, 아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(boards):  # 판 결정 후 탐색
    global answer
    visited = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    dist = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1
    dist[0][0][0] = 0

    queue = deque([[0, 0, 0]])

    while queue:
        x, y, z = queue.popleft()

        if x == 4 and y == 4 and z == 4:
            answer = min(answer, dist[x][y][z])
            if answer == 12:
                print(answer)
                exit()
            break

        for i in range(6):
            mx = x + dx[i]
            my = y + dy[i]
            mz = z + dz[i]

            if mx < 0 or my < 0 or mz < 0 or mx >= 5 or my >= 5 or mz >= 5:
                continue
            if boards[mx][my][mz] and not visited[mx][my][mz]:
                dist[mx][my][mz] = dist[x][y][z] + 1
                visited[mx][my][mz] = 1
                queue.append([mx, my, mz])


INF = int(1e9)
answer = INF


# boards 1~5층 회전 결정하기
def dfs(dir):
    global copy_boards
    if dir == 5:
        if copy_boards[4][4][4]:  # 결정되었을 때 도착지를 접근할 수 있으면 탐색
            bfs(copy_boards)
        return

    for _ in range(4):
        if copy_boards[0][0][0]:  # 출발지를 접근할 수 있는 경우에 회전
            dfs(dir + 1)
        copy_boards[dir] = rotate_clockwise(copy_boards[dir])  # 접근 못하면 회전


# boards 순서 결정하기
for order in orders:
    for i in range(5):
        copy_boards[order[i]] = boards[i]
    dfs(0)

if answer == INF:
    print(-1)
else:
    print(answer)
