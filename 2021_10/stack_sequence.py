T = int(input())

operators = ["+"]
sequence = []
numbers = [1]
top = 1

for i in range(T):
  sequence.append(int(input()))

i = 2

while sequence and top != 0:
  if numbers[-1] == sequence[0]:
    numbers.pop(-1)
    sequence.pop(0)
    operators.append("-")
    top -= 1
  else:
    numbers.append(i)
    operators.append("+")
    top += 1
    i += 1

if sequence:
  print("NO")
else:
  for i in operators:
    print(i)
