# --- 요구 사항 ---
# N개의 행성 간에 플로우 설치 (1 ≤ N ≤ 1000)
# 행성 i와 행성 j사이의 플로우 관리비용 : C[i][j] (1 ≤ i, j ≤ N)
# TODO: 모든 행성을 연결하고, 유지비용 최소화

# --- 풀이 방법 ---
# 모든 행성 연결, 양방향, 모두 연결하는 데 필요한 비용의 최솟값 -> 스패닝 트리
# 행성을 연결하는 플로우 입력값을 저장하는 배열 필요
# 부모 찾기(find) + 연결하는 함수(union) 필요
# C[0][1] + C[1][2] : 3

import sys
input = sys.stdin.readline

n = int(input())

parent = [i for i in range(n)]
edges = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(i+1):
        if i == j:
            continue
        weight = line[j]
        edges.append([i, j, weight])

edges.sort(key=lambda x: x[2])


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


answer = 0
for edge in edges:
    u, v, weight = edge

    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        answer += weight
print(answer)
