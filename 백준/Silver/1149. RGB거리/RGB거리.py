import sys
input = sys.stdin.readline

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# 모든 집을 칠하는 비용의 최솟값

# 테이블 정의 dp[i] : i번째 집까지 칠하는 비용의 최솟값 X
# 테이블 정의 dp[i][j] : i번째 집을 j색으로 칠하는 비용의 최솟값 # j==0:빨강, 1: 그린, 2: 블루

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

INF = int(1e9)
dp = [[INF for _ in range(n)] for _ in range(n)]

dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

dp[1][0] = min(dp[0][1], dp[0][2]) + arr[1][0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
print(min(dp[n-1]))
