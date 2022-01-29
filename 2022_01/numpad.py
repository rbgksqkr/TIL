import sys
from collections import deque
input = sys.stdin.readline

board = []

for _ in range(5):
  board.append(list(input().split()))


def dfs(x, y):
  start = board[x][y]
  stack = [[x, y, start]]
  numbers = []
  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]
  while stack:
    x, y, number = stack.pop()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= 5 or dy >= 5:
        continue

      temp_num = number + board[dx][dy]
      if len(number) >= 6:
        numbers.append(number)
      else:
        stack.append([dx,dy,temp_num])

  return numbers


answer = []
for i in range(5):
  for j in range(5):
    answer += dfs(i,j)

answer = list(set(answer))
print(len(answer))
