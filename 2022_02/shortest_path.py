import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF for _ in range(V+1)]
graph = [[] for _ in range(V+1)]
for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v,w))


def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0

  while queue:
    cost, cur = heapq.heappop(queue)

    if distance[cur] < cost:
      continue
    
    for i in graph[cur]:
      cost = distance[cur] + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))

  for i in range(1, len(distance)):
    if distance[i] == INF:
      print("INF")
    else:
      print(distance[i])


dijkstra(start)
