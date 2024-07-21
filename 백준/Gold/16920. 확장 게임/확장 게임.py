# --- 요구 사항 ---
# N×M인 격자. 각 칸은 비어있거나 막혀있다.
# 각 플레이어는 하나 이상의 성 소유, 이 성도 격자판 위에 있다. 한 칸에 성이 두 개 이상인 경우 x.
# 게임은 라운드로 이루어져 있고, 각 라운드마다 플레이어는 자기 턴이 돌아올 때마다 성을 확장해야 한다.
# 플레이어 1, 플레이어 2 ... 순서대로 쭉 확장.
# '.'는 빈 칸, '#'는 벽, '1', '2', ..., '9'는 각 플레이어의 성

# 각 턴이 돌아왔을 때, 플레이어는 자신이 가지고 있는 성을 비어있는 칸으로 확장한다.
#   플레이어 i는 자신의 성이 있는 곳에서 Si칸 만큼 이동할 수 있는 모든 칸에 성을 동시에 만든다.
#   위, 왼쪽, 오른쪽, 아래로 인접한 칸으로만 이동할 수 있으며, 벽이나 다른 플레이어의 성이 있는 곳으로는 이동할 수 없다.
#   성을 다 건설한 이후엔 다음 플레이어가 턴을 갖는다.

# TODO: 모든 플레이어가 더 이상 확장을 할 수 없을 때 게임이 끝난다. 게임판의 초기 상태가 주어졌을 때, 최종 상태를 구해보자.

# --- 문제 풀이 ---
# 1. 한 플레이어가 자신의 성에서 Si칸만큼 이동하며 성 만드는 함수
#   Si만큼 이동하여 성을 만든다.
# 2. 1번부터 순서대로 자신의 성을 확장해나가는 반복 함수
# 3. 빈 칸이 없는 경우
# FIXME: 전체 player 들의 값들을 queue에 저장하려다보니 퍼지고 나서 queue에 넣는 과정에서 문제 발생

import sys
from collections import deque
input = sys.stdin.readline

N, M, P = map(int, input().split())
S = [0]+list(map(int, input().split()))

board = []
players = [deque() for _ in range(P+1)]
answer = [0 for _ in range(P+1)]

for i in range(N):
    line = list(input().strip())

    for j in range(M):
        if line[j] == '.':
            line[j] = 0
        elif line[j] == '#':
            line[j] = -1
        else:
            line[j] = int(line[j])
            answer[line[j]] += 1
            players[line[j]].append([i, j])
    board.append(line)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

is_moved = True
while is_moved:
    is_moved = False
    for i in range(1, P+1):
        if not players[i]:
            continue

        queue = players[i]
        for _ in range(S[i]):
            if not queue:
                break

            for _ in range(len(queue)):
                x, y = queue.popleft()

                for d in range(4):
                    mx = x + dx[d]
                    my = y + dy[d]

                    if mx < 0 or my < 0 or mx >= N or my >= M:
                        continue

                    if board[mx][my] == -1 or board[mx][my] > 0:
                        continue

                    board[mx][my] = board[x][y]
                    answer[board[x][y]] += 1
                    queue.append([mx, my])
                    is_moved = True

print(*answer[1:])
