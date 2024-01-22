import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

k = 1
weight = arr[0]  # w / k
for i in range(1, n):
    if weight < arr[i] * (i+1):
        weight = arr[i] * (i+1)

print(weight)
