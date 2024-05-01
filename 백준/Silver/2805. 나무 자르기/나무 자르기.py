# 4 7
# 20 15 10 17
# 절단기에 설정할 수 있는 높이?
# 10 15 17 20
# maxHeight = 20
# x = 15
# -5 0 2 5 -> 7
# x = 10
# 0 5 7 10 -> 22
# ------
# 이진 탐색의 원리상 start와 end가 수렴 
# 최종적으로 start와 end가 같은 값을 가리킴
# 그러나 start와 end를 설정할 때 (start + end) // 2 연산을 수행 
# 가운데 값을 구하는 것이 아니라 더 작은 값인 start를 사용하여 연산을 진행
# 따라서, 최종적으로 start와 end가 같은 값이 되면 그 값이 최댓값이 아니라 최댓값보다 1 작은 값

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

start, end = 0, data[-1]
while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in data:
        if i - mid > 0:
            result += (i-mid)

    if result >= m:
        start = mid + 1
    elif result < m:
        end = mid - 1
print(end)
