import sys
from collections import deque
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
indegree = [0] * (V+1)

for i in range(E):
  a, b = map(int, input().split())
  graph[a].append(b) # a -> b
  indegree[b] += 1


def topology_sort():
  result = []
  queue = deque()
  # 진입차수가 0인 노드 찾기(그래프의 맨처음 찾기)
  for i in range(1, V+1):
    if indegree[i] == 0:
      queue.append(i)
  
  while queue:
    cur = queue.popleft()
    result.append(cur)
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for i in graph[cur]:
      indegree[i] -= 1
      if indegree[i] == 0:
        queue.append(i)
  

  for i in result:
    print(i, end=' ')

topology_sort()
