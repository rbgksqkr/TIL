import sys
import math
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    x, y = map(float, input().split())
    graph.append([x, y])

edges = []
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        edges.append(
            [i, j, math.sqrt(abs(graph[i][0] - graph[j][0])**2 + abs(graph[i][1] - graph[j][1])**2)])

edges.sort(key=lambda x: x[2])

parent = [i for i in range(n)]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(x, parent):
    if parent[x] != x:
        return find(parent[x], parent)
    return parent[x]


answer = 0
for edge in edges:
    u, v, w = edge

    if find(u, parent) != find(v, parent):
        union(u, v, parent)
        answer += w
print(round(answer, 2))
