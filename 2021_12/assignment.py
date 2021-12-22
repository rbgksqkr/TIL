import sys
input = sys.stdin.readline

N = int(input())
days = [0] * 1001
task = []
for _ in range(N):
  day, score = map(int, input().split())
  task.append((day,score))

task.sort(key=lambda x:(-x[1], -x[0]))

for i in range(N):
  for j in range(task[i][0]-1, -1, -1):
      if days[j] == 0:
        days[j] += task[i][1]
        break

print(sum(days))
