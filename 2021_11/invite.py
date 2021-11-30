import sys

input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
days = 1

times.sort(reverse=True)

for i in range(N):
  times[i] += i+1
print(max(times)+1)
