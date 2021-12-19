import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
planes = []
gates = [0] * G
for _ in range(P):
  planes.append(int(input()))

for i in range(P):
  flag = 0
  for j in range(planes[i]-1, -1, -1):
    if gates[j] == 0:
      gates[j] = 1
      flag = 1
      break
  if flag == 0:
    break

print(sum(gates))
