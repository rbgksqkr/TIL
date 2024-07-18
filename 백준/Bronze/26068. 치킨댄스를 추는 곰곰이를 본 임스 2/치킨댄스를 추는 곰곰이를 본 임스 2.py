import sys
input = sys.stdin.readline

n = int(input())

answer = 0
for _ in range(n):
    a, b = input().strip().split('-')

    if int(b) <= 90:
        answer += 1
print(answer)
