import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
  score = list(map(int, input().split()))
  num = score[0]
  student = score[1:]
  avg = sum(student) / num
  ace = [i for i in student if i > avg]
  percent = len(ace) / (len(student)) * 100
  ceiling = round(percent, 3)
  print(format(ceiling, ".3f")+"%")
