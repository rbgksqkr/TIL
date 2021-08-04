from sys import stdin

input = stdin.readline

n = int(input())
num = 2
sequence = []
stack = [1]
logics = ['+']

for i in range(n):
  sequence.append(int(input()))

for i in range(len(sequence)):
  if stack:
    while sequence[i] != stack[-1]:
      stack.append(num)
      num += 1
      logics.append('+')
      if stack[-1] == n:
        break      
  elif sequence[i] == num:
    logics.append('+')
    logics.append('-')
    num += 1

  if sequence[i] == stack[-1]:
    stack.pop()
    logics.append('-')

  else:
    logics.append("NO")
    break

if "NO" in logics:
  print("NO")
else:
  for i in logics:
    print(i)  
