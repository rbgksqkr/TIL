import sys
input = sys.stdin.readline

# 2
# 1 2
# 1000

T = int(input())

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m+1)]  # i를 만드는 경우의 수
    
    # 1 2
    for coin in coins:
        if coin > m:
            break
        dp[coin] += 1  # dp[2]
        for i in range(1, m+1):
            if i-coin >= 0:
                dp[i] = dp[i] + dp[i-coin]
    print(dp[m])
