import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []

a_idx = 0
b_idx = 0
while a_idx < n and b_idx < m:
    if a[a_idx] <= b[b_idx]:
        c.append(a[a_idx])
        a_idx += 1
    elif a[a_idx] > b[b_idx]:
        c.append(b[b_idx])
        b_idx += 1


if a_idx == n:
    for i in range(b_idx, m):
        c.append(b[i])
elif b_idx == m:
    for i in range(a_idx, n):
        c.append(a[i])

for i in range(n+m):
    print(c[i], end=' ')
