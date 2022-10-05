# import sys
# input = sys.stdin.readline

# n = int(input())
# counsels = [0]

# for i in range(1, n+1): # 상담 일정표 입력받기
#     t, p = map(int, input().split())
#     counsels.append((t, p))

# dp = [0 for _ in range(n+1)]
# dp[1] = counsels[1][1] # 1일차 상담 테이블 dp테이블에 입력

# for i in range(2, n+1):
#     for j in range(1, i):
#         if j + counsels[j][0] <= i and i + counsels[i][0] <= n+1:
#             dp[i] = max(dp[i], dp[j] + counsels[i][1])
    
# print(max(dp))

n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)