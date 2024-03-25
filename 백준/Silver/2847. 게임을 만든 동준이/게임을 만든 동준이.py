import sys
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

answer = 0
for i in range(n-1, 0, -1):
    if data[i] <= data[i-1]:
        gap = abs(data[i] - data[i-1]) + 1
        answer += gap
        data[i-1] -= gap
print(answer)