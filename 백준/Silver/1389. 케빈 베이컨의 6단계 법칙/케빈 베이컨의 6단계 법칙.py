from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def bfs(graph, x):
    global answer
    queue = deque([x])
    countArr = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    visited[x] = 1

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                countArr[i] = countArr[now] + 1
                queue.append(i)
    return sum(countArr)


graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = int(1e9)
result = [0]
for i in range(1, n+1):
    current_sum = bfs(graph, i)
    answer = min(answer, current_sum)
    result.append(current_sum)
print(result.index(answer))
