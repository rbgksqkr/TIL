def solution(n):
    dp = [0 for _ in range(60001)]
    dp[1] = 1
    dp[2] = 2
    plus = 0
    # k-1개 : 1가지 / k-2개 : 2가지 인데 세로로 2개놓는건 1개놓는거랑 케이스가 같으므로 1가지
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] = dp[i] % 1000000007
    return dp[i]
