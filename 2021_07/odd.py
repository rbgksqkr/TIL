from sys import stdin
numbers = []
for i in range(7):
  numbers.append(int(stdin.readline()))
odds = []
for i in numbers:
  if i % 2 == 1:
    odds.append(i)

if odds:
  print(sum(odds))
  print(min(odds))
else:
  print(-1)
