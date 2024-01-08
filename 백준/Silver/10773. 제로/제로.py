import sys

input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    m = int(input())
    if m == 0:
        data.pop()
    else:
        data.append(m)

print(sum(data))
