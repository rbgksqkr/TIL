import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
	line = list(map(int, list(input().strip())))
	board.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1
    queue = deque([[x, y]])
	
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if board[mx][my] == 1 and visited[mx][my] == 0:
                visited[mx][my] = visited[x][y] + 1
                queue.append([mx, my])
    
    return visited[n-1][m-1]

print(bfs(0, 0))