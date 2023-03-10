import sys
import heapq
input = sys.stdin.readline

n = int(input())

lectures = []
for i in range(n):
    pay, day = map(int, input().split())
    heapq.heappush(lectures, (day, pay))

result = []
while lectures:
    lecture = heapq.heappop(lectures)
    heapq.heappush(result, lecture[1])
    if lecture[0] < len(result):
        heapq.heappop(result)
print(sum(result))
