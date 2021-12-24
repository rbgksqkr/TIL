import sys
input = sys.stdin.readline
N = int(input())
arr = []
visited = [0] * N
for i in range(N):
  toStation, fillGas = map(int, input().split())
  arr.append((toStation, fillGas))
toTown, curGas = map(int, input().split())

arr.sort(key=lambda x:(-x[1], x[0]))

cur, count, idx = 0, 0, 0
while idx < len(arr):
  if toTown - cur <= curGas:
    break
  if arr[idx][0] - cur <= curGas and visited[idx] == 0:
    count += 1
    curGas -= arr[idx][0] - cur
    curGas += arr[idx][1]    
    cur += arr[idx][0] - cur 
    visited[idx] = 1
    idx = 0
  else:
    idx += 1
    
if idx >= len(arr):
  print(-1)
else:
  print(count)
