# --- 문제 분석 ---
# N×N.
# TODO: (x1, y1)부터 (x2, y2)까지 합? (x, y) : x행 y열

# 예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

# --- 문제 풀이 ---
# 표의 크기 N, 합을 구해야 하는 횟수 M
# N개의 줄의 표 정보, M개의 줄의 (x1, y1, x2, y2) 정보
# 매번 계산하면 최대 N^2*M인데, (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 로 시간초과
# 의문 : 이걸 어떻게 저장해놓지? 어떻게해야 이전 값을 이후 계산에 써먹을 수 있을까?
# FIXME: 누적합을 이용하자.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)
