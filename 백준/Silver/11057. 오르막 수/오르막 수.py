# --- 요구 사항 ---
# 오르막 수 : 수의 자리가 오름차순을 이루는 수. 인접한 수가 같아도 오름차순으로 친다.
# 예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.
# TODO: 수의 길이 N이 주어졌을 때, 오르막 수의 개수? 수는 0으로 시작할 수 있다.

# --- 풀이 방법 ---
# dp 테이블 정의[i][j] : i 자릿 수일 때 끝자리가 j인 경우 오르막 수
# 0이면 0, 1이면 0~1, 2이면 0~2, ... 9면 0~9
# dp[자리 수][앞에 오는 숫자]=경우의 수
# n번째 앞에 오는 숫자보다 n-1번째 숫자의 끝자리가 크거나 같은 경우만 체크

import sys
input = sys.stdin.readline

n = int(input())
answer = 0
dp = [[0 for _ in range(10)] for _ in range(n)]

for i in range(10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        temp = 0
        for k in range(10):
            if j > k:
                continue
            temp += dp[i-1][k]
        dp[i][j] = temp
print(sum(dp[n-1]) % 10007)
