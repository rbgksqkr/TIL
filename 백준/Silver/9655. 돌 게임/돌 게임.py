import sys
input = sys.stdin.readline

n = int(input())

dp = [-1 for _ in range(1001)]
dic = {0: 1, 1: 0}
dp[1] = 1  # dp[i] == 1 : SK / dp[i] == 0 : CY
dp[3] = 1

for i in range(2, n+1):
    if dp[i-1] != -1:
        dp[i] = dic[dp[i-1]]
    if dp[i-3] != -1:
        dp[i] = dic[dp[i-3]]

if dp[n] == 1:
    print('SK')
else:
    print('CY')