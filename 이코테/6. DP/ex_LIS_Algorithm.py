# 가장 긴 증가하는 부분 수열(LIS : Longest increasing Subsequence)
# 주어진 리스트의 값들이 증가하는 형태의 가장 긴 부분 수열을 찾는 알고리즘
# [10, 20, 10, 30, 20, 50] -> [10, 20, 30, 50] -> 4

n = 6
dp = [1] * n
array = [10, 20, 10, 30, 20, 50]

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
            print(i, dp)

print(max(dp)) # 최장길이