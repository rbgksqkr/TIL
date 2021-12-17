import sys
input = sys.stdin.readline

N = int(input())
days = [0] * 1001
score, idx = 0, 1
task = []
for _ in range(N):
  a, b = map(int, input().split())
  task.append((a,b))

task.sort(key=lambda x:(-x[1], -x[0]))

for i in range(N):
  for j in range(task[i][0]-1, -1, -1):
      if days[j] == 0:
        days[j] += task[i][1]
        break

print(sum(days))
