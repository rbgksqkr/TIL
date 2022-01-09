import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

def bfs():
  queue = deque([])

  for i in range(1, V+1):
    if visited[i] == 0: # 방문하지 않은 경우 큐 삽입
      queue.append(i)
      visited[i] = 1
      while queue: # 방문한 노드의 인접한 모든 노드 체크
        n = queue.popleft()
        for j in graph[n]:
          if visited[j] == 0:
            queue.append(j)
            visited[j] = visited[n] * -1 # 인접 노드 구분
          elif visited[j] == visited[n]: # 한 집합 내 정점끼리 인접한 경우
            return False
  return True

for _ in range(K):
  V, E = map(int, input().split())
  graph = {i:[] for i in range(1, V+1)}
  visited = [0 for _ in range(V+1)]

  for _ in range(E): # 그래프 입력
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  if bfs():
    print("YES")
  else:
    print("NO")
