def solution(n):
    dp = [0 for _ in range(2001)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n] % 1234567
