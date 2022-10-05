N, M = map(int, input().split())
frames = []

for _ in range(N):
    frames.append(list(input().strip()))


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [(x,y)]
    while stack:
        x, y = stack.pop()
        frames[x][y] = '1'
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= N or my >= M:
                continue

            if frames[mx][my] == '0':
                stack.append((mx, my))
            

count = 0
for i in range(N):
    for j in range(M):
        if frames[i][j] == '0':
            dfs(i, j)
            count += 1

print(count)

# 4 5
# 00110
# 00011
# 11111
# 00000