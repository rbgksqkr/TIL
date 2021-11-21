import sys
input = sys.stdin.readline

N = int(input())
cor = []
for i in range(N):
  a, b = map(int, input().split())
  cor.append((a,b))

cor.sort(key=lambda x:(x[1], x[0]))
print(cor)
