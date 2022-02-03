import sys
input = sys.stdin.readline

N = int(input())
maze = list(map(int, input().split()))
visited = [N for _ in range(N)]
visited[0] = 0

for i in range(N):
  for j in range(1, maze[i]+1):
    if i+j >= N:
      break
    visited[i+j] = min(visited[i+j], visited[i]+1)
  
if visited[N-1] != N:
  print(visited[N-1])
else:
  print(-1)
