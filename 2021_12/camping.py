import sys
input = sys.stdin.readline

idx = 1
while True:
  day = 0
  L, P, V = map(int, input().split())

  if L == 0 and P == 0 and V == 0:
    break

  day += L * (V // P)
  remainder = V % P
  if remainder != 0:
    if L - remainder > 0:
      day += remainder
    else:
      day += L
  print("Case "+str(idx)+": "+str(day))
  idx += 1
