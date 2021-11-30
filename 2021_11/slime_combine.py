import sys

input = sys.stdin.readline

N = int(input())
slimes = list(map(int, input().split()))
score = 0

while len(slimes) > 1:
  slimes.sort()
  score += slimes[0]*slimes[1]
  slimes[1] += slimes[0]
  slimes.pop(0)
print(score)
