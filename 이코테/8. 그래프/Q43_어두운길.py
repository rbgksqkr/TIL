def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
edges = []
parent = [i for i in range(n)]
total_cost = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    total_cost += cost
    edges.append((cost, a, b))

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(total_cost - result)






