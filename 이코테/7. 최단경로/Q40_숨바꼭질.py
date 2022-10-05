import heapq


def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(heap, (cost, i))


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = int(1e9)
distance = [INF for _ in range(n+1)]

dijkstra(1)
answer = [i for i in range(1, n+1) if distance[i] == max(distance[1:])]
print(answer[0], distance[answer[0]], len(answer))


# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
