import sys


input = sys.stdin.readline

n = int(input())
fears = list(map(int, input().split()))

# 여행을 떠날 수 있는 그룹 수의 최댓값

fears.sort()

group = 0
count = 0
for fear in fears:
    count += 1
    if fear == count:
        group += 1
        count = 0
print(group)


# 5
# 2 3 1 2 2