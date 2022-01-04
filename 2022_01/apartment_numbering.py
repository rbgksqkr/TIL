import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

visited = [[0] * N] * N
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count

    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True

answer = []
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            answer.append(count)
            count = 0

print(len(answer))
answer.sort()
for i in answer:
    print(i)
