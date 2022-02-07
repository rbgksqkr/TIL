import sys
import heapq
input = sys.stdin.readline


N = int(input())
M = int(input())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
  a, b, cost = map(int, input().split())
  graph[a].append((b, cost))
start, end = map(int, input().split())


def dijkstra(start):
  queue = []
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


dijkstra(start)
print(distance[end])
