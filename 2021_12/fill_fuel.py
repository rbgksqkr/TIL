import sys
input = sys.stdin.readline
N = int(input())
arr = []
cur = 0
count = 1
for i in range(N):
  toStation, fillGas = map(int, input().split())
  arr.append((toStation, fillGas))
toTown, curGas = map(int, input().split())

arr.sort(key=lambda x:(x[0], -x[1]))
result = []
maxGas = arr[0]

for i in range(1,N):
  if curGas >= arr[i][0] - cur:
    if maxGas[1] < arr[i][1]:
      maxGas = arr[i]
  else:
    toTown -= maxGas[0] - cur
    curGas -= maxGas[0] - cur
    curGas += maxGas[1]
    cur += maxGas[0]
    maxGas = arr[i]
    count += 1

if curGas - (maxGas[0] - cur) + maxGas[1] > toTown:
  print(count)
else:
  print(-1)
