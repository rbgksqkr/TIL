# -- 요구 사항 ---
# n가지 종류의 동전이 있으며, 각각의 동전이 나타내는 가치는 다르다.
# TODO: 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하는 경우의 수를 구하시오.
# 각각의 동전은 몇 개라도 사용할 수 있다.
# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우.

# --- 풀이 방법 ---
# dp[i] = i번째 동전을 사용하여 k원이 된 경우 + i번째 동전을 사용하지 않고 k원이 된 경우
# dp[i] : 가치의 합이 i원이 되도록 하는 경우의 수
# --- 입력 ---
# n, k (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
# 3 10
# 1
# 2
# 5
# --- 출력 ---
# 10

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in arr:
    for i in range(coin, k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])
