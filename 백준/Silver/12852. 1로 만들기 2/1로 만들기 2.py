import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
dp = [INF for _ in range(1000001)]  # dp[i] : i를 1로 만드는 최소 연산 횟수
pre = [INF for _ in range(1000001)]
dp[1] = 0
dp[2] = 1

pre[1] = 0
pre[2] = 1
for i in range(3, n+1):
    dp[i] = dp[i-1] + 1
    pre[i] = i-1
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        pre[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        pre[i] = i // 2

print(dp[n])

idx = n
while pre[idx] != INF:
    print(idx, end=' ')
    idx = pre[idx]
