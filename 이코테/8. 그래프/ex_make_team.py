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

n ,m = map(int, input().split())
operations = []
parent = [i for i in range(m+1)]

for _ in range(m):
    oper, a, b = map(int, input().split())
    operations.append((oper, a, b))


for operation in operations:
    oper, a, b = operation
    if oper == 0:
        union(parent, a, b)
    if oper == 1:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")
            

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1