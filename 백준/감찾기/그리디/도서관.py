import sys
input = sys.stdin.readline

n, m = map(int, input().split())

books = list(map(int, input().split()))
negative = []
positive = []
max_value = 0
for i in range(n):
    if books[i] < 0:
        negative.append(books[i])
    else:
        positive.append(books[i])
    max_value = max(max_value, abs(books[i]))  # 더 큰 쪽을 한번만 계산
negative.sort()
positive.sort(reverse=True)

distances = []
result = 0
for i in range(0, len(negative), m):
    if max_value != -negative[i]:
        distances.append(-negative[i])
for i in range(0, len(positive), m):
    if max_value != positive[i]:
        distances.append(positive[i])

for distance in distances:
    result += distance * 2
result += max_value
print(result)
