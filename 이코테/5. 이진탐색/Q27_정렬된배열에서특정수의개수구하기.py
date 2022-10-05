from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, x = map(int, input().split())

numbers = list(map(int, input().split()))

left = bisect_left(numbers, x)
right = bisect_right(numbers, x)

answer = right-left
if answer == 0:
    print(-1)
else:
    print(answer)

# 7 2
# 1 1 2 2 2 2 3

# 7 4
# 1 1 2 2 2 2 3