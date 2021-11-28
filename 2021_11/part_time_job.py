import sys

input = sys.stdin.readline

N = int(input())
order = [i for i in range(1, N+1)]
tip = []
answer = 0

for _  in range(N):
  tip.append(int(input()))

tip.sort(reverse=True)

for i in range(N):
  temp = tip[i] - (order[i] - 1)
  if temp > 0:
    answer += temp
  
print(answer)
