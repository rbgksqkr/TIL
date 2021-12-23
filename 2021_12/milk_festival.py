import sys
input = sys.stdin.readline
N = int(input())
markets = list(map(int, input().split()))
rule = 0
count = 0

for i in range(N):
  if markets[i] == 0 and rule == 0:
    count += 1
    rule = 1
  elif markets[i] == 1 and rule == 1:
    count += 1
    rule = 2
  elif markets[i] == 2 and rule == 2:
    count += 1
    rule = 0

print(count)
