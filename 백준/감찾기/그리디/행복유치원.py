import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

gaps = []
for i in range(1, n):
    gaps.append(numbers[i]-numbers[i-1])
gaps.sort()

for _ in range(k-1):
    gaps.pop()
print(sum(gaps))
