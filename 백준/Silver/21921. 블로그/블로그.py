import sys

# 5 2
# 1 4 2 5 1

input = sys.stdin.readline

n, x = map(int, input().split())
people = list(map(int, input().split()))
maxCount = 0
durationCount = 0

for i in range(x):
    maxCount += people[i]
durationCount += 1

count = maxCount
for i in range(x, n):
    count -= people[i-x]
    count += people[i]
    if maxCount < count:
        maxCount = count
        durationCount = 1
    elif maxCount == count:
        durationCount += 1


if maxCount == 0:
    print('SAD')
else:
    print(maxCount)
    print(durationCount)
