import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
data = []
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if graph[i][j] == 0:
                graph[i][j] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global count

    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    elif graph[x][y] == 0:
        graph[x][y] = 1
        count += 1
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True


answer = []
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer.append(count)
            count = 0


answer.sort()
print(len(answer))
for i in answer:
    print(i, end=' ')
