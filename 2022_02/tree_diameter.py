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


V = int(input())
edges = []
for i in range(1, V+1):
  temp = list(map(int, input().split()))
  for j in range(1, len(temp)-1, 2):
    edges.append((i, temp[j], temp[j+1]))
parent = [0] * (V+1)
for i in range(1, V+1):
  parent[i] = i

edges.sort(key=lambda x:-x[2])


total_cost = 0
for i in range(len(edges)):
  a, b, cost = edges[i]

  if find(a) != find(b):
    union(a, b)
    total_cost += cost

print(total_cost)
