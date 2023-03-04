import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

k, max_weight = 0, 0
for i in range(n):
    k += 1
    max_weight = max(max_weight, ropes[i] * k)
print(max_weight)
