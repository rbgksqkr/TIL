import sys
input = sys.stdin.readline

# 특정 원소의 부모노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1) 

for i in range(1, v + 1):
    parent[i] = i

edges = []
total_cost = 0
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a,b,cost))

edges.sort(key=lambda x:x[2])

for i in range(e):
  a, b, cost = edges[i]
  if find(a) != find(b):
    union(a, b)
    total_cost += cost
print(total_cost)
