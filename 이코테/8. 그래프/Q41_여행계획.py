import sys
input = sys.stdin.readline



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
parent = [i for i in range(n+1)]
edges = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            edges.append((i+1, j+1))

plans = list(map(int, input().split()))


# 노드끼리 연결하고
for edge in edges:
    a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)

# 여행계획에 있는 노드가 연결되어 있는지 확인
flag = 0
for i in range(m-1):
    a, b = plans[i], plans[i+1]
    if find(parent, a) != find(parent, b):
        flag = 1
        break

if flag == 0:
    print("YES")
else:
    print("NO")

