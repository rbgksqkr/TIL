import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
arr = [[[0, 0]]]
for _ in range(n):
    w, v = map(int, input().split())
    arr.append([w, v])

for i in range(1, n+1):
    for j in range(1, k+1):
        weight, value = arr[i]
        if j < weight:
            dp[i][j] = dp[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다
        else:
            # knapsack[i][j] = max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j]) 
            

print(dp[n][k])
