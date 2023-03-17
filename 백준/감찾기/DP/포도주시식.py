import sys
input = sys.stdin.readline

n = int(input())
cups = [0]

for _ in range(n):
    cups.append(int(input()))

dp = [0 for _ in range(10001)]
dp[1] = cups[1]
if n > 1:
    dp[2] = dp[1] + cups[2]


for i in range(3, n+1):
    dp[i] = max(dp[i-3]+cups[i-1]+cups[i], dp[i-2]+cups[i], dp[i-1])
print(dp[n])
