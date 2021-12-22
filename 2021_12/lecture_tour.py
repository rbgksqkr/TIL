import sys

input = sys.stdin.readline

n = int(input())
schedules = [0] * 10001
lectures = []
for _ in range(n):
    pay, day = map(int, input().split())
    lectures.append((pay, day))

lectures.sort(key=lambda x: (-x[0], -x[1]))

for i in range(n):
  for j in range(lectures[i][1], 0, -1):
    if schedules[j] == 0:
      schedules[j] += lectures[i][0]
      break

print(sum(schedules))
