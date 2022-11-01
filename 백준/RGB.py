n = int(input())

INF = int(1e9)
dp = [[INF] * 3 for _ in range(n)]
temp = list(map(int, input().split()))
dp[0][0], dp[0][1], dp[0][2] = temp[0], temp[1], temp[2]

for i in range(1, n):
    temp = list(map(int, input().split()))
    for j in range(3):
        if j == 0:
            dp[i][1] = min(dp[i][1], temp[1]+dp[i-1][j])
            dp[i][2] = min(dp[i][2], temp[2]+dp[i-1][j])
        if j == 1:
            dp[i][0] = min(dp[i][0], temp[0]+dp[i-1][j])
            dp[i][2] = min(dp[i][2], temp[2]+dp[i-1][j])
        if j == 2:
            dp[i][1] = min(dp[i][1], temp[1]+dp[i-1][j])
            dp[i][0] = min(dp[i][0], temp[0]+dp[i-1][j])

print(min(dp[-1]))
