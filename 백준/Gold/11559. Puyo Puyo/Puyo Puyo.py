# --- 요구 사항 ---
# 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.
# 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.
# 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터짐
# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 1연쇄가 추가된다.
# TODO: 연쇄가 몇 번 연속으로 일어날지 계산. 하나도 터지지 않는다면 0 출력.

# --- 풀이 방법 ---
# 다양한 색의 뿌요 (R, G, B, P, Y) 존재
# 1. 탐색하여 같은 색이 4개 이상이면 빈칸(`.`) 으로 만들고 count += 1
# 2. 터트린 뿌요보다 위에 있던(x값이 작은) 뿌요는 밑으로 이동시키기
# 터지는 뿌요의 위치 값 필요
# 특정 시점의 터질 수 있는 뿌요가 여러 그룹일 경우 1연쇄로 간주 -> 각각의 색마다 탐색을 돌아 다 터트리고 밑으로 이동시키기
# 3. 이동시킨 뒤에 1번 과정을 반복하여 만족하면 count += 1
# 3-2. 바로 터지지 않으면(4개 이상 모여있지 않으면) 종료

import sys
from collections import deque
input = sys.stdin.readline

boards = []
for i in range(12):
    board = list(input().strip())
    boards.append(board)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    result = [[x, y]]
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= 12 or my >= 6:
                continue

            if not visited[mx][my] and boards[mx][my] == boards[x][y]:
                visited[mx][my] = 1
                queue.append([mx, my])
                result.append([mx, my])
    return result


def deleteBlocks(blocks):
    for i, j in blocks:
        boards[i][j] = '.'


def down():  # 역순으로 반복문을 돌며 위에서 아래로 블록을 내림
    for y in range(6):
        for x in range(10, -1, -1):
            for k in range(11, x, -1):
                if boards[x][y] != "." and boards[k][y] == ".":
                    boards[k][y] = boards[x][y]
                    boards[x][y] = "."


count = 0
while True:
    visited = [[0 for _ in range(6)] for _ in range(12)]
    isBoom = False
    for i in range(12):
        for j in range(6):
            if boards[i][j] != '.' and not visited[i][j]:
                blocks = bfs(i, j)

                if len(blocks) >= 4:  # 같은 뿌요가 4개 이상이면 boom
                    isBoom = True
                    deleteBlocks(blocks)  # 기존 뿌요 터트리기

    if isBoom:
        down()  # 터트리면서 빈 공간 위에서 아래로 내리기
        count += 1
    else:
        break

print(count)
