import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
d = [0 for _ in range(n)]

d[0] = numbers[0]
for i in range(1, n):
  if d[i-1] + numbers[i] > numbers[i]:
    d[i] = d[i-1] + numbers[i]
  else:
    d[i] = numbers[i]

print(max(d))
