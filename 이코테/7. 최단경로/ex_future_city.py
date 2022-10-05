import heapq

n, m = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]

distance = [INF for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().split())

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + 1

            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(heap, (cost, i))




dijkstra(1)
one_k = distance[k]
distance = [INF for _ in range(n+1)]
dijkstra(k)
k_x = distance[x]

result = one_k + k_x

if result >= INF:
    print(-1)
else:
    print(result)


# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5