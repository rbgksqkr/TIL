# --- 문제 분석 ---
# 산성 용액과 알칼리성 용액. 각 용액에는 하나의 정수.
#   산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수.
#   알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수.
# 같은 양의 두 용액을 혼합한 용액의 특성값 : 혼합에 사용된 각 용액의 특성값의 합


# TODO: 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액 찾기

# --- 문제 풀이 ---
# N <= 100000 이므로 N^2 시간초과
# 1. n 입력받기
# 2. arr 특성값 입력받고 오름차순 정렬.
# 3. target을 빼고 합이 0에 가까운 것의 인덱스 반환
# FIXME: 투포인터인지 이분탐색인지 어떻게 판단??

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

start, end = 0, n-1

answer = arr[start] + arr[end]
answer_start, answer_end = start, end
while start < end:
    total = arr[start] + arr[end]
    if abs(answer) > abs(total):
        answer = total
        answer_start = start
        answer_end = end
    if total < 0:
        start += 1
    else:
        end -= 1

print(arr[answer_start], arr[answer_end])
