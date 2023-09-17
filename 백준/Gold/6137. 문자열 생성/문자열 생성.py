import sys
from collections import deque
input = sys.stdin.readline


def solution(inputData):
  answer = ''
  data = deque(inputData)
  count = 0 
  for _ in range(n):
    start, end = 0, len(data) - 1
    flag = 0

    while start <= end:
      if data[start] < data[end]:
        break
      elif data[start] > data[end]:
        flag = 1
        break
      else: # start == end
        start += 1
        end -= 1
    if flag == 0:
      answer += data.popleft()
    if flag == 1:
      answer += data.pop()
    count += 1
    if count % 80 == 0:
      answer += '\n'
  return answer
      

n = int(input())
inputData = []
for _ in range(n):
  inputData.append(input().strip())
  
print(solution(inputData))