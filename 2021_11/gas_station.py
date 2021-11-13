import sys

input = sys.stdin.readline

N = int(input())
roadDistance = list(map(int, input().split()))
pricePerL = list(map(int, input().split()))
price = 0

minPriceIndex = pricePerL.index(min(pricePerL[:-1]))

idx = 0
end = 0

while idx < N:
  if idx == minPriceIndex:
    price += pricePerL[minPriceIndex] * sum(roadDistance[idx:])
    break
  if pricePerL[idx] <= pricePerL[idx+1]:
    while pricePerL[idx] <= pricePerL[end]:
      end += 1
    price += pricePerL[idx] * sum(roadDistance[idx:end])
    idx += end - idx
  else:
    price += pricePerL[idx] * roadDistance[idx]
    idx += 1
  end = idx

print(price)
