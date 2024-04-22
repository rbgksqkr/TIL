import sys
input = sys.stdin.readline

n, m = map(int, input().split())
prices = []
for _ in range(m):
    prices.append(int(input()))
prices.sort()

answer = 0
max_price = 0
for idx, price in enumerate(prices):
    if n < m-idx:
        total_price = price * n
    else:
        total_price = price * (m-idx)
    if answer < total_price:
        answer = total_price
        max_price = price

print(max_price, answer)
