import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)

dp = [INF for _ in range(5001)]
dp[3] = 1
dp[5] = 1

for i in range(6, 5001):
    if dp[i-3] or dp[i-5]:
        new_data = min(dp[i-3], dp[i-5]) + 1
        dp[i] = min(dp[i], new_data)

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])
