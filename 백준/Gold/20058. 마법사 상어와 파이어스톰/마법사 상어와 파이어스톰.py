# --- 요구 사항 ---
# 2^N × 2^N인 격자
#  A[r][c]는 (r, c)에 있는 얼음의 양
# 시전할 때마다 단계 L을 결정해야 한다.

# 1. 2^L × 2^L 크기의 부분 격자로 나눈다
# 2. 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
# 3. 얼음이 있는 칸 3개 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
# 마법사 상어는 파이어스톰을 총 Q번 시전하려고 한다.
# - 남아있는 얼음 A[r][c]의 합
# - 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수


# TODO: 남아있는 얼음 A[r][c]의 합. 가장 큰 덩어리가 차지하는 칸의 개수. (단, 덩어리가 없으면 0 출력)


# --- 문제 풀이 ---
# 1. 2^L × 2^L 크기의 부분 격자로 나눈다
# - 부분 격자로 나눠서 회전 후 합치기 -> FIXME: 이걸 어떻게 해결?
# 2. 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
# 3. 얼음이 있는 칸 3개 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
# - 해당 칸이 얼음과 3개 이상 인접해 있는가? -> 아니면 -= 1

import sys
from collections import deque
input = sys.stdin.readline

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def rotate_and_melting(board, len_board, L):
    """
    Level에 맞게 회전 후 얼음을 녹임
    :param board: 보드
    :param len_board: 보드 길이
    :param L: level
    :return:
    """
    new_board = [[0] * len_board for _ in range(len_board)]  # 회전한 Board 저장 용

    # rotate
    r_size = 2 ** L  # 격자 사이즈
    for y in range(0, len_board, r_size):  # 격자 시작 좌표 y축
        for x in range(0, len_board, r_size):  # 격자 시작 좌표 x축
            for i in range(r_size):  # 열 인덱스
                for j in range(r_size):  # 행 인덱스
                    new_board[y + j][x + r_size - i - 1] = board[y + i][x + j]

    board = new_board
    melting_list = []  # 녹을 얼음 좌표
    for y in range(len_board):
        for x in range(len_board):
            ice_count = 0
            for d in range(len(dy)):
                ny = y + dy[d]
                nx = x + dx[d]

                if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board:
                    continue
                elif board[ny][nx] > 0:
                    ice_count += 1

            if ice_count < 3 and board[y][x] != 0:
                melting_list.append((y, x))

    # 저장된 얼음들을 녹임
    for y, x in melting_list:
        board[y][x] -= 1

    return board


def check_ice_bfs(board, len_board):
    """
    얼음 상태 확인
    :param board: 보드
    :param len_board: 보드 가로 길이
    :return:
    """
    used = [[False] * len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0
    for y in range(len_board):
        for x in range(len_board):
            area_count = 0
            if used[y][x] or board[y][x] == 0:
                continue
            # BFS를 이용하여 얼음 덩어리 조사
            q = deque()
            q.append((y, x))
            used[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx]  # 얼음 합 추가
                area_count += 1  # 얼음 카운트 추가

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board or used[ny][nx]:
                        continue
                    if board[ny][nx] != 0:
                        used[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count)  # 최대 얼음 덩어리 크기 파악

    print(ice_sum)
    print(max_area_count)


def solve():
    N, Q = map(int, input().split(' '))
    len_board = 2 ** N
    board = [list(map(int, input().split(' '))) for _ in range(len_board)]
    L_list = list(map(int, input().split(' ')))

    for L in L_list:
        board = rotate_and_melting(board, len_board, L)

    check_ice_bfs(board, len_board)


solve()
