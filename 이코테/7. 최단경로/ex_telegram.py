import heapq

n, m, start = map(int, input().split())
INF = int(1e9)

distance = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))



def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


dijkstra(start)

count = 0
max_time = 0
for i in range(n+1):
    if distance[i] != INF:
        count += 1
        max_time = max(max_time, distance[i])

print(count-1, max_time)
