# TODO: 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이


import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    line = list(map(int, input().split()))
    start = line[0]
    edges = line[1:-1]
    for i in range(0, len(edges), 2):
        end, weight = edges[i], edges[i+1]
        graph[start].append([end, weight])
        graph[end].append([start, weight])


def bfs(x):
    queue = deque([[x, 0]])
    visited = [0 for _ in range(n+1)]
    visited[x] = 1
    result = [0, 0]

    while queue:
        cur, cost = queue.popleft()

        for i in graph[cur]:
            next_node, next_cost = i[0], i[1]

            if not visited[next_node]:
                visited[next_node] = 1
                queue.append([next_node, cost + next_cost])
                if result[1] < cost + next_cost:
                    result = [next_node, cost + next_cost]

    return result

long_node = bfs(1)
answer = bfs(long_node[0])
print(answer[1])
