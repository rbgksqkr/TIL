import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in  range(n):
    heapq.heappush(arr, int(input()))

result = 0
while len(arr) >= 2:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    result += a + b
    heapq.heappush(arr, a + b)
print(result)