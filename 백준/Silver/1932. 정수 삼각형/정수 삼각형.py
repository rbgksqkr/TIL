import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]]
for i in range(n):
    dp.append(list(map(int, input().split())))

k = 0
for i in range(n, 0, -1):
    for j in range(n-k-1):
        dp[i-1][j] = dp[i-1][j] + max(dp[i][j], dp[i][j+1])
    k += 1

print(dp[1][0])