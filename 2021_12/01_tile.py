import sys
input = sys.stdin.readline

N = int(input())
d = [0 for i in range(1000001)]
d[1] = 1
d[2] = 2

# n-1개 타일을 놓고 1개(1) 추가
# n-2개를 놓고 2개(00) 추가 
# (11)의 경우도 2개를 놓을 수 있지만 n-1의 경우에서 카운트하기 때문에 고려하지 않는다.

for i in range(3, N+1):
  d[i] = (d[i-1] + d[i-2]) % 15746
print(d[N])
