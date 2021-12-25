import sys

input = sys.stdin.readline

T = int(input())
numberCount = [[0,0] for _ in range(41)]

numberCount[0][0] = 1
numberCount[0][1] = 0
numberCount[1][0] = 0
numberCount[1][1] = 1

for i in range(2, 41):
  numberCount[i][0] = numberCount[i-1][0] + numberCount[i-2][0]
  numberCount[i][1] = numberCount[i-1][1] + numberCount[i-2][1]

for _ in range(T):
  N = int(input())
  print(numberCount[N][0], numberCount[N][1])
