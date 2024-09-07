import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

nums = list(map(int, input().split()))
for num in nums:
    heapq.heappush(heap, num)

for i in range(1, n):
    nums = list(map(int, input().split()))
    for num in nums:
        if num > heap[0]: # heap[0]이 현재 0번째 큰 수. 새로운 num이 0번째 큰 수보다 크다면 갈아끼우기
            heapq.heappop(heap)
            heapq.heappush(heap, num)

print(heapq.heappop(heap))
