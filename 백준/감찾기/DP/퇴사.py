import sys
input = sys.stdin.readline

n = int(input())
tables = [0]
for _ in range(n):
    time, pay = map(int, input().split())
    tables.append((time, pay))

dp = [0 for _ in range(17)]
max_count = 0
for i in range(n, 0, -1):
    if i + tables[i][0] <= n+1:
        dp[i] = max(dp[i+1], dp[i+tables[i][0]] + tables[i][1])
    else:
        dp[i] = dp[i+1]
print(dp[1])
