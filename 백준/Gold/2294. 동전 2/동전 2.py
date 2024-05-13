# -- 요구 사항 ---
# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
# 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.
# 가치가 같은 동전이 여러 번 주어질 수도 있다.
# TODO: 동전의 최소 개수 출력하고, 불가능한 경우에는 -1을 출력

# --- 풀이 방법 ---
# dp[i] : i원이 되도록 하는 최소 동전의 개수

# --- 입력 ---
# 3 15
# 1
# 5
# 12
# --- 출력 ---
# 3

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

INF = int(1e9)
dp = [INF for _ in range(k+1)]

# 동전 1개만 사용했을 때 고려
dp[0] = 0

for coin in arr:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin] + 1)
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
