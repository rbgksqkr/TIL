import sys

input = sys.stdin.readline

N = int(input())
ranks = [i for i in range(1, N+1)]
expectRanks = []
count = 0

for _ in range(N):
  expectRanks.append(int(input()))

expectRanks.sort()

for i in range(N):
  count += abs(ranks[i]-expectRanks[i])

print(count)
