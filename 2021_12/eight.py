import sys
input = sys.stdin.readline
L, R = map(str, input().split())

gap = len(R) - len(L)

if gap == 0:
  count = 0
  for i in range(len(L)):
    if L[i] == R[i] and L[i] == "8":
      count += 1
  print(count)
else:
  print(0)
