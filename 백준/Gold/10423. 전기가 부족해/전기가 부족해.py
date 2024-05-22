# --- 요구 사항 ---
# 발전소 건물과 도시로 전기를 공급해 줄 케이블
# 발전소는 이미 특정 도시에 건설되어 있고, 추가적으로 드는 비용은 케이블을 설치할 때 드는 비용이 전부
# 케이블이 연결되어있는 도시에는 발전소가 반드시 하나만 존재해야 한다
# TODO: 케이블을 설치할 때 드는 비용이 굉장히 크므로 이를 최소화해서 설치하여 모든 도시에 전기를 공급하는 것

# --- 풀이 방법 ---
# 도시의 개수 N(1 ≤ N ≤ 1,000)
# 설치 가능한 케이블의 수 M(1 ≤ M ≤ 100,000)개
# 발전소의 개수 K(1 ≤ K ≤ N)개
# 발전소가 설치된 도시의 번호
# M개의 두 도시를 연결하는 케이블의 정보가 u, v, w (1 <= w <= 10,000)

# 그냥 비용이 작은 것부터 연결하는 것이 아니라 발전소가 여러개라 어디에 연결해야할지 계산해야함
# 발전소를 가장 우선수누이가 높은 0으로 지정하고, 모든 발전소를 0으로 처리하여 연결만 되면 같은 트리로 인식

import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
electrics = list(map(int, input().split()))
edges = []
parent = [i for i in range(n+1)]

for i in electrics:
    parent[i] = 0


def find(x, parent):
    if parent[x] != x:
        return find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])

count = 0
edges.sort(key=lambda x: x[2])
for edge in edges:
    u, v, w = edge

    if find(u, parent) != find(v, parent):
        union(u, v, parent)
        count += w

print(count)
