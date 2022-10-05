# from itertools import combinations
# n = int(input())

# prices = list(map(int, input().split()))


# a = []
# result = []
# for i in range(n):
#     a += list(combinations(prices, i))

# for i in range(len(a)):
#     result.append(sum(a[i]))

# result.sort()
# result = list(set(result))

# for i in range(len(result)):
#     if result[i] != i:
#         print(i)
#         break

n = int(input())
prices = list(map(int, input().split()))

prices.sort()
print(prices)

target = 1 # 1 ~ (target - 1) 까지의 금액을 모두 만들 수 있다
for price in prices:
    if target < price:
        break

    target += price

print(target)