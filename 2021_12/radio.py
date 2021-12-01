import sys

input = sys.stdin.readline

A, B = map(int, input().split())
N = int(input())

favorites = []
for _ in range(N):
  favorites.append(int(input()))

minValue = abs(B - A)
for i in range(N):
  minValue = min(minValue, abs(B-favorites[i]))

if minValue == abs(B - A):
  print(minValue)
else:
  print(1 + minValue)
