import sys
input = sys.stdin.readline

n, k = map(int, input().split())

prices = []
for _ in range(n):
    prices.append(int(input()))


prices = reversed(prices)

answer = 0
for price in prices:
    answer += k // price
    k = k % price

print(answer)
