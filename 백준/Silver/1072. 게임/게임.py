# 1 ≤ X ≤ 1,000,000,000
# 0 ≤ Y ≤ X
# z = int((y / x) * 100)

# next_z = int((y + k / x + k) * 100)
# if z !== next_z: 캐치
# FIXME: y와 x가 같을 때 0이 되는 문제 발생. z=(100*y)//x.

import sys
input = sys.stdin.readline

x, y = map(int, input().split())

# z = int((y / x) * 100)
z = (100*y)//x
start, end = 0, x
answer = -1

while start <= end:
    mid = (start + end) // 2
    result = int(((y + mid) / (x + mid)) * 100)
    if result > z:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1


print(answer)
