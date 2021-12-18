import sys
import heapq

input = sys.stdin.readline

N = int(input())
cards = []
count = 0

for _ in range(N):
    cards.append(int(input()))

heapq.heapify(cards)

for _ in range(N - 1):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a + b)
    count += a + b
print(count)
