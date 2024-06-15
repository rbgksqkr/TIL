# --- 요구 사항 ---
# K번만 위와 같이 움직일 수 있고, 그 외에는 그냥 인접한 칸으로만 움직일 수 있다.
# 맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다.
# 인접한 네 방향으로 한 번 움직이는 것, 말의 움직임으로 한 번 움직이는 것, 모두 한 번의 동작
# W, H : (1이상 200이하의 자연수), K : (0이상 30이하의 정수)
# TODO: 원숭이의 동작수의 최솟값 출력. 시작점에서 도착점까지 갈 수 없는 경우 -1 출력.

# --- 풀이 방법 ---
# K번의 제한이 있으므로 몇 번 더 말처럼 이동할 수 있는지 저장
# 말처럼 이동 가능한 횟수가 남아있다면 해당 경우의 수도 모두 queue에 저장
# 3% 틀렸습니다. -> 최초 방문 지점이 최소가 아닐 수 있다 -> 방문 배열을 사용하지 말자? -> 장애물 1을 -1로 처리하고 max값 처리
# visited를 안쓸 경우, 경우의 수가 없는 경우를 어떻게 처리?
# FIXME: 3차원 visited 배열을 선언하여 z 인덱스에 말처럼 이동 가능한 횟수를 관리

import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
m, n = map(int, input().split())
boards = []
for i in range(n):
    board = list(map(int, input().split()))
    for j in range(m):
        if board[j] == 1:
            board[j] = -1
    boards.append(board)


dir = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = [0, 0, k]
end = [n-1, m-1]


def bfs():
    queue = deque([[0, 0, k]])
    visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while queue:
        x, y, count = queue.popleft()

        if [x, y] == end:
            return visited[x][y][count]

        if count:  # 말처럼 이동
            for nx, ny in dir:
                mx = x + nx
                my = y + ny

                if mx < 0 or my < 0 or mx >= n or my >= m:
                    continue

                if not boards[mx][my] and not visited[mx][my][count-1]:
                    visited[mx][my][count-1] = visited[x][y][count] + 1
                    queue.append([mx, my, count-1])

        for i in range(4):  # 인접 공간 이동
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if not boards[mx][my] and not visited[mx][my][count]:
                visited[mx][my][count] = visited[x][y][count] + 1
                queue.append([mx, my, count])

    return -1


print(bfs())
