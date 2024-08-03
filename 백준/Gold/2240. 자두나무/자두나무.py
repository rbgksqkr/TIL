# 매 초마다, 두 개의 나무 중 하나의 나무에서 열매가 떨어지게 된다.
# 자두는 하나의 나무 아래에 서 있다가 다른 나무 아래로 빠르게 움직일 수 있다.
# 하지만 자두는 체력이 그다지 좋지 못해서 많이 움직일 수는 없다.

# 자두는 T(1≤T≤1,000)초 동안 떨어지게 된다. 자두는 최대 W(1≤W≤30)번만 움직이고 싶어 한다.
# 매 초마다 어느 나무에서 자두가 떨어질지에 대한 정보가 주어졌을 때, 자두가 받을 수 있는 자두의 개수를 구해내는 프로그램을 작성하시오.
# 자두는 1번 자두나무 아래에 위치해 있다고 한다.

# --- 풀이 방법 ---
# 1. W를 3차원 배열로 담고 현재 위치에서 이동할 경우 -1 하기
# dp[i][j][W] : i초일 때 j 위치에서 W번 움직였을 때 받은 최대 자두 개수
# FIXME: dp[i][j] : i초 지났을 때, j 번 움직여서 먹을 수 있는 최대 자두 수

import sys
input = sys.stdin.readline

t, w = map(int, input().split())
data = [0] + [int(input()) for _ in range(t)]
dp = [[0 for _ in range(w+1)] for _ in range(t+1)]
for i in range(1, t+1): # 1번 자리에 계속 있는 케이스 처리
    if data[i] == 1:
        dp[i][0] = dp[i-1][0]+1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, w+1): 
        # 1번에서 떨어졌는데 짝수번 움직인 경우 || 2번에서 떨어졌는데 홀수번 움직인 경우 : +1
        if (data[i] == 1 and j % 2 == 0) or (data[i] == 2 and j % 2 != 0):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[t]))
