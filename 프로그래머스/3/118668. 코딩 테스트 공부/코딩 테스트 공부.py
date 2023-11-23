# 1. 어떻게 정렬할 지(어떤 걸 선택할 지)
# 2. 그 문제를 풀 수 있을만큼 힘 기르기 (첫 문제)
# 3. 문제 풀기 vs 힘 기르기 비교
# 4. 어떤 문제를 풀 지 결정  (두 번째 이후)
# 5. 풀 수 있는 문제 중 가장 이득인 거 따로 저장
# => 못품 => DP
        
def solution(alp, cop, problems):
    answer = 0
    INF = int(1e9)
    target_alp, target_cop = -1, -1
    for problem in problems:
        target_alp = max(target_alp, problem[0])
        target_cop = max(target_cop, problem[1])
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)    
    n = target_alp
    m = target_cop
    dp = [[INF for _ in range(m+1)] for _ in range(n+1)]
    
    dp[alp][cop] = 0
    for i in range(alp, n+1):
        for j in range(cop, m+1):
            if i + 1 <= n:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j + 1 <= m:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    cal_alp, cal_cop = i+alp_rwd, j+cop_rwd
                    if cal_alp >= n: cal_alp = n
                    if cal_cop >= m: cal_cop = m

                    dp[cal_alp][cal_cop] = min(dp[cal_alp][cal_cop], dp[i][j] + cost)
                    
    return dp[n][m]
    
    
    return answer