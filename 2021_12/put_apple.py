import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())
cor = []
front = 0
back = M
distance = 0
for _ in range(J):
  cor.append(int(input()))


for i in range(J):
  if back < cor[i]:
    front += cor[i] - back
    distance += cor[i] - back
    back += cor[i] - back
  elif front > cor[i]: 
    distance += front - (cor[i]-1)
    front -= front - (cor[i]-1)
    back = front + M  
  elif front == cor[i]:
    front -= 1
    back -= 1 
    distance += 1    
  else:
    continue
print(distance)
