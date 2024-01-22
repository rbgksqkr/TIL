import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

count = 0
for i in range(n-1, -1, -1):
    count += k // coins[i]
    k %= coins[i]
print(count)