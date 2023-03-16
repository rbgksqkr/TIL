import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[0 for _ in range(15)] for _ in range(15)]

    for i in range(1, 15):
        dp[0][i] = i

    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[k][n])
