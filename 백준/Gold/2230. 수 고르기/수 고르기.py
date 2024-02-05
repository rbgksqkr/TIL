import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
start, end = 0, 0
result = int(2e9)
while start <= end and end < n:
    diff = arr[end] - arr[start]
    if diff < m:
        end += 1
    else:
        result = min(result, diff)
        start += 1
print(result)

