import sys
input = sys.stdin.readline
L, R = map(str, input().split())

gap = len(R) - len(L)
count = 0
if gap == 0:
  if L[0] != R[0]:
    print(0)
  else:
    if L[0] == "8":
      count += 1

    for i in range(1, len(L)):
      if L[i] != R[i]:
        break
      elif L[i] == R[i] and L[i] == "8":
        count += 1
    print(count)
else:
  print(0)
