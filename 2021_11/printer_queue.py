from collections import deque

T = int(input())
for i in range(T):
  count = 0
  N, M = map(int, input().split())
  prio = deque(map(int, input().split()))
  while True:
    if [i for i in prio if prio[0] < i]:
      prio.rotate(-1)
    else:
      prio.popleft()
      count += 1
      if M == 0:
        break
    M -= 1
    if M < 0:
      M = len(prio) - 1
  print(count)
