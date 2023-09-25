import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int ,input().split()))
cards.sort()

answer = []

def binary_search(left, right, target):
  while left <= right:
    mid = (left + right) // 2
    if cards[mid] == target:
      return 1
    elif cards[mid] < target:
      left = mid + 1
    else:
      right = mid -1
  return 0

for number in numbers:
  print(binary_search(0, n-1, number), end=' ')