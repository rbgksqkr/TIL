import sys
import heapq
input = sys.stdin.readline

# 보석 개수, 가방 개수
n, k = map(int, input().split())

gems = []
# 보석 무게, 보석 가격
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(gems, (m, v))

bags = []
# 가방 최대 수납 무게
for _ in range(k):
    c = int(input())
    bags.append(c)
bags.sort()

result = 0
temp_gems = []
for bag in bags:
    while gems and bag >= gems[0][0]:
        heapq.heappush(temp_gems, -heapq.heappop(gems)[1])
    if temp_gems:
        result -= heapq.heappop(temp_gems)
    elif not gems:
        break
print(result)
