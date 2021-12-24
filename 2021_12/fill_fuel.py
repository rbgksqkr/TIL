import sys
import heapq

input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    heapq.heappush(arr, list(map(int, input().split())))
toTown, curGas = map(int, input().split())

count = 0
move = []

while curGas < toTown:
  while arr and arr[0][0] <= curGas:
    toStation, fillGas = heapq.heappop(arr)
    heapq.heappush(move, [-fillGas, toStation])

  if not move:
    count = -1
    break
  
  fg, ts = heapq.heappop(move)
  curGas += -fg
  count += 1

if toTown <= curGas:
  print(count)
else:
  print(-1)
