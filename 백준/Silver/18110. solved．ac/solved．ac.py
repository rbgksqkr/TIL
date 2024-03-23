import sys
input = sys.stdin.readline


def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())
condition = roundUp(n * 0.15)

data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

if n == 0:
    print(0)
else:
    result = data[condition:n-condition]
    answer = sum(result) / len(result)
    print(roundUp(answer))
