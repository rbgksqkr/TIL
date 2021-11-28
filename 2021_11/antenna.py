import sys

input = sys.stdin.readline

N = int(input())
cor = list(map(int, input().split()))
cor.sort()

if len(cor) % 2 == 0:
  print(cor[len(cor)//2 - 1])
else:
  print(cor[len(cor)//2])
