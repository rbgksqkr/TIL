n, m = map(int, input().split())

weights = list(map(int, input().split()))
balls = [0 for _ in range(m+1)]
for weight in weights:
    balls[weight] += 1

result = 0
for i in range(1, m+1):
    n -= balls[i]
    result += balls[i] * n
print(result)