import sys

input = sys.stdin.readline

N = int(input())
cur = input().strip()
light = input().strip()

result_1 = 0
result_2 = 0

def switchNumber(n):
  if n == "0":
    return "1"
  else:
    return "0"

# 0번째 스위치를 누른 경우
zeroClick = switchNumber(cur[0]) + switchNumber(cur[1]) + cur[2:]
result_1 += 1
for i in range(1, N):
  if zeroClick[i-1] != light[i-1]:
    if i == N-1:
      zeroClick = zeroClick[:i-1] + switchNumber(zeroClick[i-1]) + switchNumber(zeroClick[i])
    else:
      zeroClick = zeroClick[:i-1] + switchNumber(zeroClick[i-1]) + switchNumber(zeroClick[i]) + switchNumber(zeroClick[i+1]) + zeroClick[i+2:]
    result_1 += 1

if zeroClick != light:
  result_1 = -1

# 0번째 스위치를 안누른 경우
for i in range(1, N):
  if cur[i-1] != light[i-1]:
    if i == N-1:
      cur = cur[:i-1] + switchNumber(cur[i-1]) + switchNumber(cur[i])
    else:
      cur = cur[:i-1] + switchNumber(cur[i-1]) + switchNumber(cur[i]) + switchNumber(cur[i+1]) + cur[i+2:]
    
    result_2 += 1   

if cur != light:
  result_2 = -1

if result_1 >= 0 and result_2 >= 0:
  print(min(result_1, result_2))
elif result_1 < 0 and result_2 >= 0:
  print(result_2)
elif result_1 >= 0 and result_2 < 0:
  print(result_1)
else:
  print(-1) 
