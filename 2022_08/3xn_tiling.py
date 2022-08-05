def solution(n):
    dp = [0 for _ in range(5001)]
    dp[1] = 1
    dp[2] = 3
    plus = 0
    # 2씩 늘어날 때마다 *3 + 2 맞왜틀?
    # 특수 경우에 대해 타일을 앞에 놓을 지, 뒤에 놓을 지 2가지 경우가 있음 ;;
    for i in range(4, n+1, 2):
        dp[i] += dp[i-2] * 3 + plus + 2
        plus += dp[i-2] * 2
    return dp[n] % 1000000007
