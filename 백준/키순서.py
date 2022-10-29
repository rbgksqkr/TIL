import sys
input = sys.stdin.readline

n,m = map(int, input().split())
INF = int(1e9)
distances = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    distances[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            distances[i][j] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        

answer = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if distances[i][j] != INF or distances[j][i] != INF:
            count += 1
    if count == n:
        answer += 1
print(answer)
