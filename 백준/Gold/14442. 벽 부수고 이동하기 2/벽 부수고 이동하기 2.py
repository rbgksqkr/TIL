# --- 요구 사항 ---
# NxM 격자. 0 : 빈칸, 1 : 벽
# (1, 1)에서 (N, M) 최단경로로 이동 (맵에서 가장 적은 개수의 칸을 지나는 경로)
# 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다.
# TODO: 최단 거리를 출력하고, 불가능할 때는 -1을 출력

# --- 풀이 방법 ---
# visited 3차원 방문 배열을 만들고, z 인덱스에 K개까지 부술 수 있는 벽의 개수 저장
# visited[mx][my][mz-1] = visited[x][y][z] + 1
# 탐색이 끝난 후 최솟값을 출력하고, 불가능할 때는 -1 출력

import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
boards = [list(map(int, list(input().strip()))) for _ in range(n)]

INF = int(1e9)
visited = [[[INF]*(k+1) for _ in range(m)]
           for _ in range(n)]  # 최솟값을 구하므로 INF로 초기화

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([[0, 0, k]])
    visited[0][0][k] = 1

    while queue:
        x, y, count = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][count]  # 맨 처음 도달한 경우가 최솟값

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            # 벽 안부수고 가기
            # 빈 칸 & 방문하지 않은 경우
            if not boards[mx][my] and visited[mx][my][count] == INF:
                visited[mx][my][count] = visited[x][y][count] + 1
                queue.append([mx, my, count])

            # 벽 부수기
            # 벽 & 벽을 부수고 방문하지 않은 경우
            if boards[mx][my] and count > 0 and visited[mx][my][count-1] == INF:
                visited[mx][my][count-1] = visited[x][y][count] + 1
                queue.append([mx, my, count-1])
    return -1


answer = bfs()
print(answer)
