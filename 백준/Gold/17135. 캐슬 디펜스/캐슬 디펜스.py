# --- 문제 분석 ---
# N×M 격자판.
# 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나
# 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.

# 성을 적에게서 지키기 위해 '궁수 3명 배치'
# 궁수는 성이 있는 칸에 배치 가능 / 하나의 칸에는 최대 1명의 궁수
# 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격
# 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적
#   그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적 공격
#   같은 적이 여러 궁수에게 공격당할 수 있다.
#   공격받은 적은 게임에서 제외된다.
#   궁수의 공격이 끝나면, 적이 이동한다.
# 적은 아래로 한 칸 이동
#   성이 있는 칸으로 이동한 경우에는 게임에서 제외된다.
#   모든 적이 격자판에서 제외되면 게임이 끝난다.

# 0은 빈 칸, 1은 적이 있는 칸
# (r1, c1), (r2, c2)의 거리 : |r1-r2| + |c1-c2|

# 궁수를 배치한 이후의 게임 진행은 정해져있다.
# TODO: 궁수의 공격으로 제거할 수 있는 적의 최대 수 출력


# --- 문제 풀이 ---
# 1. 입력 : 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D
# 2. 완전 탐색으로 궁수 3명을 N+1번 행의 배치 (백트래킹 or 조합)
# 3. 거리가 D 이하인 적 중 가장 가까운 적 중 가장 왼쪽에 있는 적 공격
# - * 거리 계산
# - 거리 : |r1-r2| + |c1-c2|, [i][j] 중 j가 작은 적
# - 모든 궁수의 공격이 끝난 후, 공격 받은 적은 격자판에서 지우기
# - 나머지 적은 아래로 이동
# - 아래로 이동했을 때 n번째면 제거
# FIXME: 개복잡함

# 조건 1. 격자 판 N*M, 각 칸당 적의 최대 수 1
# 조건 2. 궁수 3명 배치. 성이 있는 칸에 배치할 수 있고, 한칸에 최대 수 1
# 조건 3. 턴마다 궁수는 적하나 공격 가능, 모든 궁수 동시 공격
# 조건 4. 공격 거리 D이하, 여럿이면 왼쪽부터 공격하고 공격 받으면 적은 판에서 제거
# 조건 5. 공격이 끝나면 1칸씩 전진, 아래로 1칸 이동하고 성이 있는 칸으로 이동하면 판에서 제거 -> 적이 아니라 궁수가 올라가도 동일

import sys
from itertools import combinations
from collections import deque
from copy import deepcopy


def hunt(archer):
    boards = deepcopy(board)  
    visited = [[0] * M for _ in range(N)]  
    cnt = 0
    for i in range(N-1, -1, -1):  # 한칸씩 전진(적이 아닌 궁수가 전진) (조건5)
        die = []
        for m in archer:  # 뽑은 궁수 자리에 대해 (조건2)
            queue = deque([[i, m, 1]])
            while queue:
                y, x, d = queue.popleft()
                if boards[y][x]:
                    die.append([y, x])
                    if not visited[y][x]:
                        visited[y][x] = 1
                        cnt += 1  # 죽였으니 점수 증가
                    break

                if d < D:  # 사정거리보다 짧으면 (조건4)
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= ny < N and 0 <= nx < M:
                            queue.append([ny, nx, d+1])  # 거리 증가

        for y, x in die:  # (조건3) 모든 궁수가 동시에 공격하니 마지막에 처리
            boards[y][x] = 0

    return cnt


N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split()))
         for _ in range(N)]  # (조건 1)
move = [[-1, 0], [0, -1], [1, 0]]
result = 0
for archer in combinations([i for i in range(M)], 3):  # (조건2)
    result = max(result, hunt(archer))
print(result)
