# TODO: 전화번호 목록이 일관성이 있는지 없는지를 구하기
# 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.

# T, n, 전화번호 목록을 입력받는다.
# 전화번호 목록을 순회하면서 다른 번호의 접두어가 되는지 확인 -> 접두어가 되면 False

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(input().strip())
    arr.sort()

    answer = 0
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            answer = 1
            break

    if answer:
        print('NO')
    else:
        print('YES')
