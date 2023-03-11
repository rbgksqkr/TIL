import sys
input = sys.stdin.readline

n = int(input())
balls = input().strip()

red, blue = 0, 0
for i in range(n):
    if balls[i] == 'R':
        red += 1
    else:
        blue += 1
result = min(red, blue)

count = 1
for i in range(1, n):
    if balls[0] != balls[i]:
        break
    count += 1
if balls[0] == 'R':
    result = min(result, red - count)
else:
    result = min(result, blue - count)


count = 1
for i in range(n-2, -1, -1):
    if balls[-1] != balls[i]:
        break
    count += 1
if balls[-1] == 'R':
    result = min(result, red - count)
else:
    result = min(result, blue - count)

print(result)
