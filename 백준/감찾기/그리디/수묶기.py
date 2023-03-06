import sys
input = sys.stdin.readline

n = int(input())

numbers = []
negative = []
positive = []
one = 0
for _ in range(n):
    number = int(input())
    if number < 1:
        negative.append(number)
    elif number > 1:
        positive.append(number)
    else:
        one += 1


# 양수 : 큰 수부터 2개씩 묶기 / 음수 : 작은 수부터 2개씩 묶기
# 더할거야 곱할거야
# 1개 남으면 어캄
# 그냥 더해

positive.sort(reverse=True)
negative.sort()
result = 0

if len(positive) % 2 == 0:  # 짝수
    for i in range(0, len(positive)-1, 2):
        result += positive[i] * positive[i+1]
else:  # 홀수
    for i in range(0, len(positive)-1, 2):
        result += positive[i] * positive[i+1]
    result += positive[-1]

if len(negative) % 2 == 0:
    for i in range(0, len(negative)-1, 2):
        result += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        result += negative[i] * negative[i+1]
    result += negative[-1]

print(result+one)
