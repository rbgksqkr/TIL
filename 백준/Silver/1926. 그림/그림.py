from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if board[mx][my] and not visited[mx][my]:
                visited[mx][my] = 1
                count += 1
                queue.append([mx, my])
    return count


result = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            result.append(bfs(i, j))

if result:
    print(len(result))
    print(max(result))
else:
    print(0)
    print(0)
