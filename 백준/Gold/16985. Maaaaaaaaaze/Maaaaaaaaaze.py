# -- 요구사항 ---
# 5×5 크기의 판이 5개
# 주어진 판들을 시계 방향, 혹은 반시계 방향으로 자유롭게 회전 가능
# 판을 쌓는 순서 자유
# 입구 : 정육면체에서 참가자가 임의로 선택한 꼭짓점에 위치한 칸
# 출구 : 입구와 면을 공유하지 않는 꼭짓점에 위치한 칸 (대각선 정반대)
# TODO: 가장 적은 이동 횟수? 모든 경우에 탈출을 못하면 -1 출력

# --- 풀이 방법 ---
# 1. 판 결정 (4방향 회전 고려 : 4)
# 2. 쌓는 순서 결정 (5개의 판 순서 결정 : 5! = 125) orders : [0, 1, 2, 3, 4]
# 3. 입구, 출구 결정 (4개의 꼭짓점 순회 : 4)
# 4. 탐색 (5 * 5 * 5 = 125)
# => 4 * 125 * 4 * 125 = 1000 * 1000 = 백만

# 판이 결정된 상태에서 임의의 입구, 출구 결정해서 탐색로직부터 짜기 (O)
# 판 돌리는 함수 구현 (O)
# 각각의 판을 돌린 후 탐색 (O)
# 쌓는 순서 결정

import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

# boards 3차원 배열 저장
boards = []
for _ in range(5):
    board = [list(map(int, input().split())) for _ in range(5)]
    boards.append(board)
copy_boards = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
orders = list(permutations([0, 1, 2, 3, 4], 5))


def rotate_clockwise(board):
    temp = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[j][4-i] = board[i][j]
    return temp


# 방향 : 상, 하, 좌, 우, 위, 아래
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
# 입구 출구 결정
# start = [[0, 0, 0], [0, 4, 0], [4, 0, 0], [4, 4, 0]]
# end = [[4, 4, 4], [4, 0, 4], [0, 4, 4], [0, 0, 4]]


def dfs(dir):
    global copy_boards
    if dir == 5:
        if copy_boards[4][4][4]:
            bfs(copy_boards)
        return

    for _ in range(4):
        if copy_boards[0][0][0]:
            dfs(dir + 1)
        copy_boards[dir] = rotate_clockwise(copy_boards[dir])


# boards 순서 결정하기
for order in orders:
    # a, b, c, d, e = order
    # copy_boards_order = [boards[a], boards[b],
    #                      boards[c], boards[d], boards[e]]
    # boards 회전시키기
    # 5개의 board 각각을 회전
    for i in range(5):
        copy_boards[order[i]] = boards[i]
    dfs(0)
    # 4방향으로 회전 (4번 회전하면 원상태)
    # for j in range(4):
    #     rotate_clockwise(copy_boards_order[i])
    #     # 판이 결정된 후, 입구와 출구에 들어갈 수 있으면 탐색 시작
    #     # 돌리니까 모든 대각선을 고려할 필요 없이 0, 0, 0 에서 4, 4, 4 로 가면 됨
    #     if copy_boards_order[0][0][0] and copy_boards_order[4][4][4]:
    #         bfs(copy_boards_order)
if answer == INF:
    print(-1)
else:
    print(answer)
