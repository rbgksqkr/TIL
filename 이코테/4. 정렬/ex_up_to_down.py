n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.sort(reverse=True)

for number in numbers:
    print(number, end=' ')


# 3
# 15
# 27
# 12