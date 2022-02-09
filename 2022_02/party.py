import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
for _ in range(M):
  a, b, times = map(int, input().split())
  graph[a].append((b, times))


def dijkstra(start):
  queue = []
  distance = [INF for i in range(N+1)]
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


times = [[]]
for i in range(1, N+1):
  times.append(dijkstra(i))

answer = []
for i in range(1, N+1):
  answer.append(times[i][X] + times[X][i])
print(max(answer))
