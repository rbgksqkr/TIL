import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
v1, v2 = map(int, input().split())


def dijkstra(start):
  queue = []
  distance = [INF for _ in range(N+1)]
  heapq.heappush(queue, (0, start))
  distance[start] = 0

  while queue:
    dist, cur = heapq.heappop(queue)
    if distance[cur] < dist:
      continue
    for i in graph[cur]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))

  return distance


count = 0
start = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

path_1 = start[v1] + from_v1[v2] + from_v2[N]
path_2 = start[v2] + from_v2[v1] + from_v1[N]

total = min(path_1, path_2)

if total >= INF:
  print(-1)
else:
  print(total)
