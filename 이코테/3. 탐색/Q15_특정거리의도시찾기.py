import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


n, m, k, x = map(int, input().split())
INF = int(1e9)
distance = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))

dijkstra(x)


flag = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = 1
if flag == 0:
    print(-1)

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4