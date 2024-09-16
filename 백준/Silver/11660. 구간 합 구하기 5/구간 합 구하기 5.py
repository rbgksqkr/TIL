# --- 문제 분석 ---
# N×N.
# TODO: (x1, y1)부터 (x2, y2)까지 합? (x, y) : x행 y열

# --- 문제 풀이 ---
# 표의 크기 N, 합을 구해야 하는 횟수 M
# N개의 줄의 표 정보, M개의 줄의 (x1, y1, x2, y2) 정보
# 매번 계산하면 최대 N^2*M인데, (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 로 시간초과

# 의문 : 이걸 어떻게 저장해놓지? 어떻게해야 이전 값을 이후 계산에 써먹을 수 있을까?
# FIXME: 누적합 이용하기
# 두 점 사이의 직사각형에 해당하는 표의 합 구하기
# dp[i][j] = (0, 0)부터 (i, j)까지의 누적합
# 표의 일부분 구하는 방법 : dp[x2][y2] - 나머지 부분

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        # 0~i행, j-1열 + i-1행, 0~j열 - i-1행, j-1열 + arr[i-1][j-1](자기자신))
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # x1, y1, x2, y2로 만든 직사각형보다 하나 큰 직사각형을 만들고, 나머지를 뺀다.
    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)
