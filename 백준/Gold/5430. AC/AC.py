from collections import deque
import sys
# 테스트 케이스 개수 T 입력
# 수행할 함수 p
# 배열 길이 n
# [1,2,3,4] 배열이 주어짐 -> 해당 배열에 대해 함수 p를 수행했을 때 결과값 출력
# R은 모든 원소 뒤집기, D는 맨앞 원소 삭제
# 배열이 비어있을 때 D 수행 시 error 출력
# ---
# RDD
# 4
# [1, 2, 3, 4]
# 입력받은 배열 [1, 2, 3, 4] 에 RDD를 수행한다
# R -> [4, 3, 2, 1]
# D -> [3, 2, 1]
# D -> [2, 1]

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    p = list(input().strip())
    n = int(input())
    data = input().strip()

    arr = deque(data[1:-1].split(','))
    isError = False
    isReverse = False
    if n == 0:
        arr = deque()
    arr = deque([i.strip() for i in arr])

    for i in p:
        if i == 'R':
            isReverse = not isReverse

        elif i == 'D':
            if len(arr) == 0:
                print('error')
                isError = True
                break
            if isReverse:
                arr.pop()
            elif not isReverse:
                arr.popleft()
    if not isError:
        if isReverse:
            arr.reverse()
        print(f"[{','.join(arr)}]")
