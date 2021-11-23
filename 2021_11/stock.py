import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  stock = list(map(int, input().split()))
  benefit = 0
  maxPrice = 0

  for i in range(len(stock)-1, -1, -1):
    if stock[i] > maxPrice:
      maxPrice = stock[i]
    else:
      benefit += maxPrice-stock[i]
    
  print(int(benefit))
