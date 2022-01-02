import sys
input = sys.stdin.readline

N = int(input())
T = int(input())

graph = {i:[] for i in range(1,N+1)}

for i in range(T):
  x, y = map(int, input().split())
  graph[x].append(y) 
  graph[y].append(x)  

for key in graph:
  graph[key].sort() 

visited = [0] * (N+1)
count = 0
stack = [1]
while stack:
  cur = stack.pop()
  if visited[cur] != 1:
    visited[cur] += 1
    count += 1
    stack += reversed(graph[cur])

print(count-1)
