# 지렁이는 인접한 네 방향의 다른 배추로 이동 가능.
# 카테고리 : 인접하지 않은 영역 개수 세기

# TODO: 최소의 배추흰지렁이 마리 수?

# 1. T 입력받기. 가로(m), 세로(n), 배추개수 입력받기.
# 2. nxm 2차원 배열을 만들고 배추 위치를 배열에 삽입
# 3. 배추 위치 바탕으로 인접하지 않은 영역 개수 세기
# 4. 방문 배열과 카운팅 변수를 전역에 두고 탐색이 끝날 때마다 += 1

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())

    # 2. nxm 2차원 배열을 만들고 배추 위치를 배열에 삽입
    board = [[0]*m for _ in range(n)]
    for _ in range(k):
        b, a = map(int, input().split())
        board[a][b] = 1

    visited = [[0]*m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 3. 배추 위치 바탕으로 인접하지 않은 영역 개수 세기
    def dfs(x, y):
        visited[x][y] = 1

        for i in range(4):
            mx, my = x+dx[i], y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if not visited[mx][my] and board[mx][my]:
                dfs(mx, my)

    # 4. 방문 배열과 카운팅 변수를 전역에 두고 탐색이 끝날 때마다 += 1
    answer = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)
