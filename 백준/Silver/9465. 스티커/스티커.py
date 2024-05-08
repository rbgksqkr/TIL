# --- 요구 사항 ---
# 스티커 2n개를 구매
# 스티커는 2행 n열로 배치
# 스티커 한 장을 떼면, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.
# 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
# TODO: 상냥이가 뗄 수 있는 스티커의 점수의 최댓값?

# --- 풀이 방법 ---
# FIXME: 다이나믹 프로그래밍의 핵심은 DP배열이 가지는 의미 & DP배열을 계산하는 방법
# N-1번째 어떤 선택을 했더라도 항상 마지막 N열에서 하나를 더 고를 수 있기 때문에,
# 최댓값은 항상 마지막 N열에서 스티커를 고르는 경우를 한정
# DP[0][-1]과 DP[1][-1]중의 최댓값

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    graph = []
    dp = [[0 for _ in range(n)] for _ in range(2)]

    for _ in range(2):
        graph.append(list(map(int, input().split())))

    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]

    if n == 1:
        print(max(dp[0][-1], dp[1][-1]))
        continue

    dp[0][1] = graph[1][0] + graph[0][1]
    dp[1][1] = graph[0][0] + graph[1][1]

    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    else:
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + graph[0][i]
            dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + graph[1][i]

        print(max(dp[0][-1], dp[1][-1]))
