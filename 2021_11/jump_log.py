import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for i in range(T):
  N = int(input())
  L = list(map(int, input().split()))
  L2 = deque([])
  result = []

  L.sort()
  L2.append(L.pop())

  while L:
    if len(L) % 2 == 0:
      number_1 = L.pop()
      number_2 = L.pop()
      L2.appendleft(number_1)
      L2.append(number_2)
    else:
      number = L.pop()
      L2.append(number)

  for i in range(N-1):
    result.append(abs(L2[i+1] - L2[i]))
  result.append(abs(L2[0]-L2[-1]))
  print(max(result))
