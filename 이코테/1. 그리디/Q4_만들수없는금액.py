n = int(input())
coins = list(map(int, input().split()))
coins.sort()

answer = coins[0]


for i in range(1, n):
    if answer + 1 < coins[i]:
        answer = answer + 1
        break
    if i == n-1:
        answer += coins[i] + 1
    else:
        answer += coins[i]
print(answer)
