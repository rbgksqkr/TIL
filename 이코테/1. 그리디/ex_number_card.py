n, m = map(int, input().split())
cards = []
min_nums = []
for i in range(n):
    temp = list(map(int, input().split()))
    min_nums.append(min(temp))

print(max(min_nums))


# 3 3
# 3 1 2
# 4 1 4
# 2 2 2