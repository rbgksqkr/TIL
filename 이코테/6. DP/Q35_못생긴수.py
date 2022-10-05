n = int(input())

dp = [0 for _ in range(1001)]

result = [1, 2, 3, 5]
mul = 2

for i in range(n//3):
    for j in range(1,4):
        result.append(result[j]*mul)
    mul += 1
result.sort()
result = list(set(result))
print(result[n-1])
