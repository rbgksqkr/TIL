import heapq
import sys
input = sys.stdin.readline


n = int(input())
arr = []
for _ in range(n):
    target = int(input())
    if target > 0:
        heapq.heappush(arr, target)
    elif target == 0:
        if len(arr) > 0:
            print(heapq.heappop(arr))
        else:
            print(0)
