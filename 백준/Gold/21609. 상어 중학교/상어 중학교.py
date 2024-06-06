# --- 요구 사항 ---
# N×N 보드
# 모든 칸에는 블록이 하나씩 들어있고, 블록은 검은색 블록, 무지개 블록, 일반 블록이 있다.
# 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현한다. 검은색 블록은 -1, 무지개 블록은 0으로 표현한다.
# 블록 그룹은 연결된 블록의 집합이다. 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다.
# 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다.
# 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.
# 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
# 오토 플레이 기능 개발
# - 크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
# - 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B^2점을 획득한다.
# - 격자에 중력이 작용한다.
# - 격자가 90도 반시계 방향으로 회전한다.
# - 다시 격자에 중력이 작용한다.
# TODO: 오토 플레이가 모두 끝났을 때 획득한 점수의 합

# --- 문제 풀이 ---
# 1. 크기가 가장 큰 블록 그룹 찾기
# - 모든 보드를 탐색하여 가장 큰 블록 그룹 찾기
# - maxCount 값을 가진 블록 그룹이 여러 개라면 무지개 블록 수가 많은 블록
# - 그런 블록 그룹이 여러개라면 행이 가장 큰 것, 그 다음은 열이 가장 큰 블록 그룹 찾기
# 2. 1에서 찾은 블록 그룹의 모든 블록을 제거하고, 점수 counting
# 3. 중력 작용하고, 90도 반시계 방향으로 돌리고, 중력 작용
# - 격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다. 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

boards = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, color):
    queue = deque([[i, j]])
    visited[i][j] = 1
    blocks, rainbows = [[i, j]], []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if not visited[mx][my]:
                if boards[mx][my] == 0:
                    queue.append([mx, my])
                    rainbows.append([mx, my])
                    visited[mx][my] = 1
                elif boards[mx][my] == color:
                    queue.append([mx, my])
                    blocks.append([mx, my])
                    visited[mx][my] = 1

   # 무지개블록은 다른 블록 그룹에서도 사용되기 때문에 방문 해제
    for i, j in rainbows:
        visited[i][j] = 0

    # [그룹에 속한 블록의 개수는 2 이상, 무지개 블록 개수 정렬, 전체 블록 그룹]
    return [len(blocks+rainbows), len(rainbows), blocks+rainbows]


def gravity(graph):  # 중력 함수
    for i in range(n-2, -1, -1):
        for j in range(n):
            if graph[i][j] != -1:
                pointer = i

                # 다음 블록이 경계가 아니고, 빈 칸(-2)이면 내리기
                while pointer + 1 < n and boards[pointer + 1][j] == -2:
                    boards[pointer][j], boards[pointer +
                                               1][j] = boards[pointer+1][j], boards[pointer][j]
                    pointer += 1


def rotate90(graph):  # 반시계 회전 함수
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[n-1-j][i] = graph[i][j]
    return new_graph


score = 0

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    answer_blocks = []

    for i in range(n):
        for j in range(n):
            if boards[i][j] > 0 and not visited[i][j]:
                block_result = bfs(i, j, boards[i][j])
                if block_result[0] >= 2:
                    answer_blocks.append(block_result)
    answer_blocks.sort(reverse=True)

    # 블록 그룹이 없을 경우 break
    if not answer_blocks:
        break

    # 블록 지우고 점수 획득
    for x, y in answer_blocks[0][2]:
        boards[x][y] = -2
    score += answer_blocks[0][0]**2

    # 중력
    gravity(boards)

    # 반시계 90도 회전
    boards = rotate90(boards)

    # 중력
    gravity(boards)

print(score)
