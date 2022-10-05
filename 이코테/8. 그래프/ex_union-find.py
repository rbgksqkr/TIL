############## union-find 알고리즘 ##################
# 1. find : 최상위 부모를 찾아 부모테이블에 저장. cycle판별 가능.
# 2. union : 두 노드를 연결. 보통 find를 해서 같은 집합이 아닌 경우 실행.
###################################################

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


v, e = map(int, input().split())


parent = [i for i in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)

for i in range(1, v+1):
    print(find(parent, i), end = ' ')

print()

for i in range(1, v+1):
    print(parent[i], end= ' ')