import sys
from collections import deque
input = sys.stdin.readline

# 건물 짓는 순서가 정해진 방향 그래프이고
# 순서가 있어 사이클이 없어서 위상정렬의 조건을 만족한다.
# 이수체계도와 같이 먼저 해야 하는 순서대로 하나씩 처리할 때,
# 위상정렬 알고리즘을 사용할 수 있다는 것을 파악해야 한다.

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
cost = [0] * (N+1)
for i in range(1, N+1):
  temp = list(map(int, input().split()))
  cost[i] = temp[0]
  for j in range(1, len(temp)-1):
    graph[temp[j]].append(i)
    indegree[i] += 1


def topology_sort():
  result = [0] * (N+1)
  queue = deque()

  for i in range(1, N+1):
    if indegree[i] == 0:
      queue.append(i)
  
  while queue:
    cur = queue.popleft()
    # 선수 건물 짓는데 걸리는 시간이 저장되어 있음
    # 현재 건물 짓는데 걸리는 시간 더하기
    result[cur] += cost[cur]
    print(result, cur, cost, graph)
    for i in graph[cur]:
      indegree[i] -= 1
      # i번째 건물 짓기 전에 지어야 하는 선수 건물 짓는데 걸리는 시간 저장
      result[i] = max(result[i], result[cur])
      if indegree[i] == 0:
        queue.append(i)
  
  return result


answer = topology_sort()
for i in range(1, N+1):
  print(answer[i])
