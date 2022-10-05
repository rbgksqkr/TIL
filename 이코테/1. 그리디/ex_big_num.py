import sys

input = sys.stdin.readline
result = 0
N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
count = 0
for _ in range(M):
    if count >= K:
        result += numbers[1]
        count = 0
    else:
        result += numbers[0]
        count += 1
print(result)
    