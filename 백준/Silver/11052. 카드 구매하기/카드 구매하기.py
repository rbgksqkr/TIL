# 카드팩의 종류는 카드 N개가 포함된 카드팩과 같이 총 N가지가 존재
# 돈을 최대한 많이 지불해서 카드 N개 구매하려고 한다. 카드가 i개 포함된 카드팩의 가격은 Pi원이다.
# 카드 N개를 갖기 위해 지불해야 하는 금액의 최댓값
# 금액의 최댓값을 배열로 저장

# dp[i] = 카드 i개를 구매하는 최대 가격
# packs[k] = 카드 k개가 포함된 k원짜리 카드팩

import sys
input = sys.stdin.readline

n = int(input())
packs = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]


answer = []
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + packs[j])
print(dp[n])
