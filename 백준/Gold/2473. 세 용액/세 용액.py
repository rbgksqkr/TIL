# --- 요구 사항 ---
# 같은 양의 세 가지 용액을 혼합한 용액의 특성값 : 혼합에 사용된 각 용액의 특성값의 합
# 세 종류의 알칼리성 용액만으로나 혹은 세 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.
# TODO: 같은 양의 세 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 세 용액 찾기?

# --- 풀이 방법 ---
# N은 3 이상 5,000 이하. N^2 까진 가능.
# 수의 범위가 -1,000,000,000 이상 1,000,000,000 이하
# 어떤 3개를 뽑아야 특성값이 0에 가까울까? N^2으로 2개를 뽑고 그거를 0으로 만드는 것을 찾는 건 어때? -> N^2 * logN
# -97 -6 -2 6 98
# ex) -97, -6 을 뽑고, 가장 0에 가깝게 만드는 특성값을 뽑기. 반복.
# FIXME: 2개를 미리 뽑고, 1개를 이분탐색하는걸 생각했음. 그것보다 기준 1개를 미리뽑고 2개의 숫자 합으로 이분탐색.

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
answer = sys.maxsize
numbers.sort()
result = []
for i in range(n-2):
    start = i + 1  # 기준점 다음부터 탐색
    end = n - 1
    while start < end:
        # 세 가지 용액을 혼합한 용액의 특성값
        total = numbers[i] + numbers[start] + numbers[end]

        if answer > abs(total):
            answer = abs(total)
            # 특성값이 0에 가까운 세 용액 저장
            result = [numbers[i], numbers[start], numbers[end]]
        if total <= 0:
            start += 1
        elif total > 0:
            end -= 1
        else:
            break

print(result[0], result[1], result[2])
