import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()

for i in range(n-1):
    times[i+1] += times[i]
print(sum(times))
