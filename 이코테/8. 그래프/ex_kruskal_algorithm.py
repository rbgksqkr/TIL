###### union-find ######

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

################### 크루스칼 알고리즘 ###########################
# 1. 양방향 그래프이므로 순서없이 리스트에 모든 간선 정보 저장
# 2. 가중치를 기준으로 오름차순 정렬
# 3. union-find 알고리즘을 통해 cycle 판별 후 발생하지 않으면 연결
#############################################################
v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges= []
result = 0

# 1. 모든 간선 정보 저장
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 2. 가중치를 기준으로 오름차순 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 3. 부모 노드가 같으면 cycle 발생
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)



# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25