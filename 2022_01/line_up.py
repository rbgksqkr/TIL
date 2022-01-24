import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for i in range(E):
  a, b = map(int, input().split())
  graph[a].append(b) # a -> b

def topology_sort():
    N = len(graph)
    stack = [] 
    visited = [0 for _ in range(N)] 
    for i in range(1, N):
      if visited[i] == 0:
          dfs(i, stack, visited)
    
    result = []
    while len(stack) != 0:
        result.append(stack.pop())
    for i in result:
      print(i, end=' ')

def dfs(v, stack, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0: 
          dfs(i, stack, visited)
    stack.append(v)

topology_sort()
