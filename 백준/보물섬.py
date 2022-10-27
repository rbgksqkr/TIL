from collections import deque
n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(input().strip()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    distance = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if data[mx][my] == 'L':
                if visited[mx][my] == 0:
                    visited[mx][my] = 1
                    distance[mx][my] = distance[x][y] + 1
                    queue.append((mx, my))

    answer = 0
    for i in distance:
        answer = max(answer, max(i))
    return answer

result = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)
