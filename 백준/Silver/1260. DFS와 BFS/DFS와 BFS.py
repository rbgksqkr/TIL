# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.


# TODO: 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성

# n, m, v 입력
# m번 입력

import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 양방향 간선
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, visited):
    visited[x] = 1
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i, visited)


def bfs(x):
    queue = deque([x])
    visited = [0 for _ in range(n+1)]
    visited[x] = 1

    while queue:
        x = queue.popleft()

        print(x, end=' ')

        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)


visited = [0 for _ in range(n+1)]

dfs(v, visited)
print()
bfs(v)
