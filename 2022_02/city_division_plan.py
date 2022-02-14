import sys
input = sys.stdin.readline

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]


def union(a, b):
  a = find(a)
  b = find(b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b


N, M = map(int, input().split())
edges = []
for _ in range(M):
  a, b, c = map(int, input().split())
  edges.append((a,b,c))

edges.sort(key=lambda x:x[2])

parent = [0] * (N+1)
for i in range(1, N+1):
  parent[i] = i

total_cost = 0
big_cost = 0
for i in range(M):
  a, b, cost = edges[i]
  if find(a) != find(b):
    union(a, b)
    big_cost = max(big_cost, cost)
    total_cost += cost
print(total_cost-big_cost)
