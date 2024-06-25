# --- 요구사항 ---
# 국가예산의 총액은 미리 정해져 있음. 모든 예산요청을 배정해 주기 어려움.
# 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정
# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 '정수 상한액'을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
# - 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
# ex) 전체 국가예산이 485.예산요청 120, 110, 140, 150.
# 상한액을 127로 잡으면, 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대.
# TODO: 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산 배정?

# --- 문제 풀이 ---
# N은 3 이상 10,000 이하. 이 값들은 모두 1 이상 100,000 이하. M은 N 이상 1,000,000,000 이하 -> 이진탐색
# mid 값을 정수 상한액으로 가정하고, 그 상한액으로 전체 국가예산을 만족하는지 판단.
# 만족하는 mid값의 max값 구하기

import sys
input = sys.stdin.readline
N = int(input())
requests = list(map(int, input().split()))
deposit = int(input())

answer = 0
start = 1  # 예산이 1 이상
end = int(1e9)  # 100000 이 최댓값이 될수도 있으므로 100000으로 잡으면 위험
requests.sort()

if sum(requests) <= deposit:  # 1. 모든 요청 배정 가능
    answer = requests[-1]
else:  # 2. '정수 상한액'을 계산
    while start <= end:
        mid = (start + end) // 2

        count = 0
        for request in requests:
            if request > mid:
                count += mid
            else:
                count += request

        if count <= deposit:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
print(answer)
