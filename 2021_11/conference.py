import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
conferences = deque()
for _ in range(N):
  a, b = map(int, input().split())
  conferences.append((a, b))

fastEndConf = deque(sorted(conferences, key=lambda x:(x[1],x[0])))
shortConf = fastEndConf.popleft()
count = 1
while fastEndConf:
  if shortConf[1] > fastEndConf[0][0]:
    fastEndConf.popleft()
  else:
    shortConf = fastEndConf.popleft()      
    count += 1
    
print(count)
