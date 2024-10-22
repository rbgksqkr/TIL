# 가장 큰 증가하는 부분 수열의 합
# dp[i] : i번째 까지 가장 큰 증가하는 부분 수열의 합
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [1, 101, 0, 0, 0, 0, 0, 0, 0, 0]
# [1, 101, 3, 0, 0, 0, 0, 0, 0, 0]
# [1, 101, 3, 53, 0, 0, 0, 0, 0, 0]
# [1, 101, 3, 53, 113, 0, 0, 0, 0, 0]

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [0 for _ in range(1001)]

dp[0] = numbers[0]

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+numbers[i])
        else:
            dp[i] = max(dp[i], numbers[i])

print(max(dp))
