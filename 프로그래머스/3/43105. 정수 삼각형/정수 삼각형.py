# [n][m] => [n+1][m], [n+1][m+1]
import copy
def solution(triangle):
    answer = 0
    n, m = len(triangle), len(triangle[-1])
    dp = copy.deepcopy(triangle)
    
    for i in range(n-1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])
    
    return max(dp[-1])