import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [INF for _ in range(v+1)]
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            next_node, cost = i[0], i[1]

            if dist + cost < distance[next_node]:
                distance[next_node] = dist + cost
                heapq.heappush(queue, (dist+cost, next_node))

    return distance


start = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

path_1 = start[v1] + from_v1[v2] + from_v2[v]
path_2 = start[v2] + from_v2[v1] + from_v1[v]

total = min(path_1, path_2)

if total >= INF:
    print(-1)
else:
    print(total)