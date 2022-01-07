import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([N])
graph = [0] * 100001
graph[N] = 1

def bfs():
  while graph[K] == 0:
    cur = queue.popleft()
    if cur*2 < 100001:
      if graph[cur*2]:
        graph[cur*2] = min(graph[cur*2], graph[cur]+1)
      else:
        graph[cur*2] = graph[cur] + 1
      queue.append(cur*2)

    if graph[cur+1]:
      graph[cur+1] = min(graph[cur+1], graph[cur]+1)  
    else:
      graph[cur+1] = graph[cur] + 1
    queue.append(cur+1)

    if graph[cur-1]:
      graph[cur-1] = min(graph[cur-1], graph[cur]+1)
    else:
      graph[cur-1] = graph[cur] + 1
    queue.append(cur-1) 
 
bfs()
print(graph[K]-1)
