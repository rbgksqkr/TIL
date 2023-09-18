import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())

answer = 0
left = 0
right = n - 1
data.sort()

while left < right:
  result = data[left] + data[right]
  if result == x:
    answer += 1
    left += 1
  elif result < x:
    left += 1
  else:
    right -= 1
print(answer)