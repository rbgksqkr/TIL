import sys
input = sys.stdin.readline

# 1. **테이블 정의하기**
# 2. **점화식 찾기**
# 3. **초기값 정하기**

# 테이블 : 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을 때 점수 합의 최댓값, 단 i번째 계단은 반드시 밟아야 함
# dp[k][1] : k번째 계단에 1개의 계단을 연속해서 밟은 최댓값 => k-2에서 2칸 이동
n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
dp = [[0 for _ in range(3)] for _ in range(301)]
if n == 1:
    print(arr[1])
else:
    dp[1][1] = arr[1]
    dp[2][1] = arr[2]
    dp[2][2] = dp[1][1] + arr[2]
    for i in range(3, n+1):
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + arr[i]
        dp[i][2] = dp[i-1][1] + arr[i]
    print(max(dp[n][1], dp[n][2]))
