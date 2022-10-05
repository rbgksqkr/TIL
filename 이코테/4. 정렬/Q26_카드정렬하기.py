import sys
import heapq

input = sys.stdin.readline
n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

result = 0
for i in range(n-1):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a+b)
    result += a+b

print(result)