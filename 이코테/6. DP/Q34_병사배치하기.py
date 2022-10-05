# n명의 병사가 무작위로 나열
# 전투력을 내림차순으로 배치
# 병사를 열외시키는 방법으로 정렬


n = int(input())

dp = [1] * n
attacks = list(map(int, input().split()))
attacks.reverse()

for i in range(1, n):
    for j in range(0, i):
        if attacks[j] < attacks[i]:
            dp[i] = max(dp[i], dp[j]+1)
            print(i, dp)

print(n-max(dp))