import sys

input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
  numbers.append(list(map(int, input().split())))


for i in range(1,N):
  for j in range(i+1):
    if j == 0:
      numbers[i][j] += numbers[i-1][0]
    elif j == i:
      numbers[i][j] += numbers[i-1][-1]
    else:
      numbers[i][j] += max(numbers[i-1][j-1], numbers[i-1][j])

print(max(numbers[-1]))
