import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

for target in b:
    start, end = 0, n-1
    isExist = False		# 찾음 여부

    # 이분탐색 시작
    while start <= end:		# start가 end보다 커지면 반복문 탈출
        mid = (start + end) // 2  # mid는 start와 end의 중간값
        if target == a[mid]:  # target(목표값)이 A[mid]값과 같다면 (목표값 존재여부를 알았다면)
            isExist = True
            print(1)
            break
        elif target > a[mid]:  # A[mid]가 target보다 작으면 큰 부분에서 탐색
            start = mid + 1
        else:			# A[mid]가 target보다 크다면 작은 부분에서 탐색
            end = mid - 1

    if not isExist:
        print(0)
