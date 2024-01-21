import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [-1]
arr += list(map(int, input().split()))
dp = [0 for _ in range(100001)]
dp[0] = 0
for i in range(1, n+1):
    dp[i] = dp[i-1] + arr[i]

for _ in range(m):
    start, end = map(int, input().split())
    print(dp[end]-dp[start-1])
