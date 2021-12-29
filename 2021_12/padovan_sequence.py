import sys
input = sys.stdin.readline

T = int(input())
d = [0 for i in range(101)]
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2

for i in range(6, 101):
  d[i] = d[i-1] + d[i-5]

for _ in range(T):
  N = int(input())
  print(d[N])
