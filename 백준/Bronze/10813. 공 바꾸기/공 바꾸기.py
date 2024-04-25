import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i], graph[j] = graph[j], graph[i]
print(*graph[1:])
