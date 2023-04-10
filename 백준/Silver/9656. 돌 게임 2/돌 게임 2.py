import sys
input = sys.stdin.readline

n = int(input())

dp = [-1 for _ in range(1001)]

dp[1] = 1
dp[2] = 0
dp[3] = 1


def flip(x):
    if x == 1:
        return 0
    if x == 0:
        return 1


for i in range(4, n+1):
    if dp[i-3] != -1:
        dp[i] = flip(dp[i-3])
    elif dp[i-1] != -1:
        dp[i] = flip(dp[i-1])

if dp[n] == 1:
    print('CY')
else:
    print('SK')
