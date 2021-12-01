import sys

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
C = int(input())
calories = []

for _ in range(N):
  calories.append(int(input()))
calories.sort(reverse=True)

temp = 0
pizza = C // A
for i in range(N):
  temp += calories[i]
  pizza = max(pizza, (C + temp) // (A + B*(i+1)))
print(pizza)
