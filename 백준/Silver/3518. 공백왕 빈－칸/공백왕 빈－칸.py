import sys
input = sys.stdin.readline


answer = []
n = 1001
m = 0
for _ in range(n):
  sentense = input().strip().split()
  m = max(m, len(sentense))
  answer.append(sentense)

answer_length = [0 for _ in range(m+1)]

for i in range(n):
  for j in range(len(answer[i])):
    answer_length[j] = max(answer_length[j], len(answer[i][j]) + 1)

result = []
for i in range(n):
  temp = ''
  for j in range(len(answer[i])):
    temp += answer[i][j]
    black_length = answer_length[j] - len(answer[i][j])
    temp += black_length * ' '
  result.append(temp)

for i in range(n):
  print(result[i].rstrip())