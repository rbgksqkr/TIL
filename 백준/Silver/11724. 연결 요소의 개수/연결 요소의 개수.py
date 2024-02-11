import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]


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


for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

s = set()
for i in range(1, n+1):
    s.add(find(i))
print(len(s))
