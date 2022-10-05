n, m = map(int, input().split())

prices = []
d = [10001 for _ in range(10001)]

# for _ in range(n):
#     price = int(input())
#     d[price] = 1
#     idx = 1
#     while price * idx <= m:
#         target = price * idx
#         d[target] = min(d[target], d[target-price] + 1)
#         idx += 1

for _ in range(n):
    prices.append(int(input()))

d[0] = 0
for i in range(n):
    for j in range(prices[i], m+1):
        if d[j-prices[i]] != 10001: # 2돌고나서 3돌 때 d[6] = min(d[6], d[6-3] + 1) = min(3, 2) = 2
            d[j] = min(d[j], d[j-prices[i]] + 1) # 2가 돌아서 d[2] = 1, d[4] = 2 / j가 5일때, d[5] = d[5-3] + 1 = 2

if d[m] == 10001:
    print(-1)
else:
    print(d[m])            


# 2 15
# 2
# 3