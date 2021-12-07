import sys
input = sys.stdin.readline
T = int(input())

fibo = [0,1]
for i in range(2,46): 
    fibo.append(fibo[i-1] + fibo[i-2])

for _ in range(T):
    N = int(input())
    result = []
    for i in range(45,0,-1):
      if fibo[i] <= N:
        result.append(fibo[i])
        N = N - fibo[i]
        if N == 0:
          for i in range(len(result)-1, -1, -1):
            print(result[i], end=" ")
          break
