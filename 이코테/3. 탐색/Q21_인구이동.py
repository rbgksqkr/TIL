from collections import deque

n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    united = [] # 연합
    united.append((x, y))
    visited[x][y] = 1
    total = data[x][y] # 연합의 인구수
    count = 1 # 연합을 이루고 있는 칸의 개수
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            if l <= abs(data[mx][my]-data[x][y]) <= r and visited[mx][my] == 0:
                visited[mx][my] = 1
                united.append((mx, my))
                queue.append((mx, my))
                total += data[mx][my]
                count += 1

    for i, j in united:
        data[i][j] = total // count


answer = 0
while True:
    visited = [[0]*n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j)
                idx += 1
    if idx == n*n:
        break

    answer += 1
print(answer)
