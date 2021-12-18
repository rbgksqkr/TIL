import sys

input = sys.stdin.readline

N = int(input())
minus_arr = []
plus_arr = []
ones = []
result = 0

for i in range(N):
    num = int(input())
    if num == 1:
        ones.append(num)
    elif num > 1:
        plus_arr.append(num)
    else:
        minus_arr.append(num)

plus_arr.sort(reverse=True)
minus_arr.sort()

if len(plus_arr) % 2 == 0:
    for i in range(0, len(plus_arr), 2):
        result += plus_arr[i] * plus_arr[i + 1]
else:
    for i in range(0, len(plus_arr) - 1, 2):
        result += plus_arr[i] * plus_arr[i + 1]
    result += plus_arr[-1]

if len(minus_arr) % 2 == 0:
    for i in range(0, len(minus_arr), 2):
        result += minus_arr[i] * minus_arr[i + 1]
else:
    for i in range(0, len(minus_arr) - 1, 2):
        result += minus_arr[i] * minus_arr[i + 1]
    result += minus_arr[-1]

print(result + sum(ones))
