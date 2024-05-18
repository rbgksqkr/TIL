import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = []
b = []
answer = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        answer[i][j] = a[i][j] + b[i][j]

for line in answer:
    print(*line)
