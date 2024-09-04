# --- 문제 분석 ---
# TODO: 가장 긴 증가하는 부분 수열 출력

# --- 문제 풀이 ---
# 6
# 10 20 10 30 20 50

# dp
# 1
# 1 2
# 1 2 2
# 1 2 2 3
# 1 2 2 3 3
# 1 2 2 3 3 4
# dp[i] = i번째 인덱스까지 증가하는 부분 수열 길이

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * (n+1)

# 10 20 10 30 20 50
for i in range(len(arr)):
    for j in range(i):  # j: 0부터 i-1까지
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

maxValue = max(dp)
print(maxValue)

answer = []
for i in range(n-1, -1, -1):
    if dp[i] == maxValue:
        answer.append(arr[i])
        maxValue -= 1

answer.sort()
print(*answer)
