# NxN.
# 1은 집이 있는 곳을, 0은 집이 없는 곳
# 탐색 후 탐색한 범위의 개수를 반환 후 정렬

# TODO: 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

# 1. n 입력받기.
# 2. 입력값으로 2차원 배열 만들기.
# 3. dfs 탐색 후 집 개수 반환
# 4. 정렬 후 출력

import sys
input = sys.stdin.readline

n = int(input())

# 2. 입력값으로 2차원 배열 만들기.
board = []
for _ in range(n):
    line = list(map(int, list(input().strip())))
    board.append(line)

visited = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global count
    visited[x][y] = 1

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or my < 0 or mx >= n or my >= n:
            continue

        if not visited[mx][my] and board[mx][my]:
            count += 1
            dfs(mx, my)


# 3. dfs 탐색 후 집 개수 반환
answer = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j]:
            count = 1
            dfs(i, j)
            answer.append(count)

# 4. 정렬 후 출력
answer.sort()
print(len(answer))
for i in answer:
    print(i)
