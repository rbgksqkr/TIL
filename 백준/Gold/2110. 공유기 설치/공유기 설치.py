# TODO: C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리의 최댓값?

# 1. n, c 를 입력받는다.
# 2. 집의 좌표를 입력받는다.
# 3. 가장 인접한 두 공유기 사이의 거리 최댓값 -> x거리만큼 간격을 정했을 때 공유기를 c개 이상 놓을 수 있는가?
# 4. start = 0, end = 맨 끝 집과 맨 첫 집 사이의 거리
# 5. mid를 간격으로 정하고, mid이상 떨어진 집에 설치 count += 1
# 6. count가 c 이상이면 설치 & end = mid - 1, c 미만이면 start = mid - 1

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []

for _ in range(n):
    houses.append(int(input()))

houses.sort()

# 4. left = 0, right = 맨 끝 집과 맨 첫 집 사이의 거리
start = 1
end = houses[-1] - houses[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    prev = houses[0]
    count = 1  # 첫 집에 설치

    for i in range(1, n):
        # 5. mid를 간격으로 정하고, mid이상 떨어진 집에 설치 count += 1
        if houses[i] - prev >= mid:
            count += 1
            prev = houses[i]

    # 6. count가 c 이상이면 설치 & end = mid - 1, c 미만이면 start = mid - 1
    if count >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
