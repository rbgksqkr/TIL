import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 초대할 동기의 수
count = 0
visited = [False] * (n + 1)
# 상근이의 친구 탐색
for i in graph[1]:
    if not visited[i]:
        count += 1
        visited[i] = True
# 상근이 친구의 친구 탐색
    for j in graph[i]:
        if not visited[j] and j != 1:
            count += 1
            visited[j] = True

print(count)
