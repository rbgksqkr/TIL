import sys
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)


def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0
  while queue:
    dist, cur = heapq.heappop(queue)

    if distance[cur] < dist:
      continue
    
    for i in graph[cur]:
      cost = dist + 1
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(queue, (cost, i))


dijkstra(X)
if K not in distance:
  print(-1)
else:
  for i in range(len(distance)):
    if distance[i] == K:
      print(i)
