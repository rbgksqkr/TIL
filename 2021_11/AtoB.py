import sys

input = sys.stdin.readline

A, B = map(int, input().split())
count = 0

while A < B:
  if B % 10 != 1 and B % 2 != 0:
    break
  if B % 10 == 1:
    B = B // 10
    count += 1
  elif B % 2 == 0:
    B = B // 2
    count += 1

if A == B:
  print(count+1)
else:
  print(-1)
