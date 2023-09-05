from collections import deque

    
def solution(board):
    n = len(board)
    m = len(board[0])
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                x, y = i, j
    
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1

    def bfs(x, y):
        queue = deque([[x, y]])
        while queue:
            x, y = queue.popleft()

            if board[x][y] == 'G':
                return visited[x][y]

            for i in range(4):
                nx, ny = x, y
                while True:
                    mx = nx + dx[i]
                    my = ny + dy[i]
                    if mx < 0 or my < 0 or mx >= n or my >= m or board[mx][my] == 'D':
                        break
                    nx, ny = mx, my

                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
        return -1
            
    answer = bfs(x, y)
    if answer > 0:
        answer -= 1
    return answer