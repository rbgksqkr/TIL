# 상하좌우. 뭉쳐있는 병사 개수 카운팅.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(m):
    line = input().strip()
    graph.append(list(line))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, target):
    global visited, count
    visited[x][y] = 1
    
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or my < 0 or mx >= m or my >= n:
            continue

        if not visited[mx][my] and graph[mx][my] == target:
            count += 1
            dfs(mx, my, target)



visited = [[0 for _ in range(n)] for _ in range(m)]

answer = {'W': 0, 'B': 0}

for i in range(m): # 100
    for j in range(n): # 100
        if not visited[i][j]:
            count = 1
            visited[i][j] = 1
            dfs(i, j, graph[i][j])
            answer[graph[i][j]] += count**2

print(answer['W'], answer['B'])
            