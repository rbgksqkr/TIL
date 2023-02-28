import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1 for _ in range(m)] for _ in range(n)]


def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for i in range(4):
        mx, my = x + dx[i], y + dy[i]

        if mx < 0 or my < 0 or mx >= n or my >= m:
            continue

        if graph[x][y] > graph[mx][my]:
            ways += dfs(mx, my)

    dp[x][y] = ways
    return dp[x][y]


print(dfs(0, 0))
