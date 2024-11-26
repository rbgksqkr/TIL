import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b, weight = map(int, input().split())
  graph[a].append([b, weight])
  graph[b].append([a, weight])


def bfs(x):
  queue = deque()
  queue.append([x, 0])
  visited = [0 for _ in range(n+1)]
  visited[x] = 1
  result = [0, 0]
  while queue:
    cur, cost = queue.popleft() # cur번 노드까지 든 비용 : cost
    for i in graph[cur]:
      next_num, value = i[0], i[1] # cur에서 next_num번 노드까지 가는 비용 : value
      if visited[next_num] == 0:
        visited[next_num] = 1
        queue.append([next_num, cost + value]) # 시작노드부터 next_num번 노드까지 가는 비용
        if result[1] < cost + value: # 더 먼 노드가 있으면 대입.
          result[0] = next_num
          result[1] = cost + value

  return result


long_node = bfs(1)          # 1번이 루트노드니까 1번부터 제일 먼 노드를 찾고,
answer = bfs(long_node[0])  # 그 노드에서 제일 먼 노드를 찾는다.
print(answer[1])