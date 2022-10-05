from collections import deque

N, M = map(int, input().split())
mazes = []

for _ in range(N):
    mazes.append(list(map(int, list(input().strip()))))


def bfs(x, y):
    queue =deque([(x, y)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1   
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= N or my >= M:
                continue

            if mazes[mx][my] == 1 and visited[mx][my] == 0:
                mazes[mx][my] = mazes[x][y] + 1
                queue.append((mx, my))


bfs(0, 0)
print(mazes[N-1][M-1])





# bfs(0, 0)

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111