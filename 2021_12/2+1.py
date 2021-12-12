import sys
input = sys.stdin.readline
N = int(input())
price = []
cost = 0
for _ in range(N):
  price.append(int(input()))

price.sort()

while price:
  sets = []
  for _ in range(3):
    if price:
      sets.append(price.pop())
    else:
      break
  if len(sets) == 3:
    sets.pop()
  cost += sum(sets)

print(cost)
