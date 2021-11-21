import sys
input = sys.stdin.readline

N = int(input())
cor = []
for i in range(N):
  a, b = map(int, input().split())
  cor.append((a,b))

cor.sort(key=lambda x:(x[0], x[1]))

for i in cor:
  print(i[0], i[1])
