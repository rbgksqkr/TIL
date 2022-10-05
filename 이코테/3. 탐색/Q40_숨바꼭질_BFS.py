from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


start = 1
distance = [-1 for _ in range(n+1)]
distance[start] = 0

queue = deque([start])

while queue:
    now = queue.popleft()

    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            queue.append(i)

print(distance)
