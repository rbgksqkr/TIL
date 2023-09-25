import sys
input = sys.stdin.readline

k, m = map(int, input().split())

lines = []
for _ in range(k):
  lines.append(int(input()))
lines.sort()

def binary_search(left, right, target):
  while left <= right:
    mid = (left + right) // 2
    count = 0
    for line in lines:  
      count += line // mid
    if count >= target:
      left = mid + 1
    else:
      right = mid - 1
  print(right)

binary_search(1, lines[-1], m)