import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

INF = int(1e9)
distance = [INF for _ in range(v+1)]
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance[start] = 0


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        weight, now = heapq.heappop(queue)

        if distance[now] < weight:
            continue

        for i in graph[now]:
            next, cost = i[0], i[1]
            if distance[now] + cost < distance[next]:
                distance[next] = distance[now] + cost
                heapq.heappush(queue, (distance[next], next))


dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
