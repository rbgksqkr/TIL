import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = list(map(int, input().split()))

answer = 0
# 탐색해야 하는 값 : 블루레이 크기
# start : 가능한 블루레이 크기 중 최솟값 -> max(times)
# end : 가능한 블루레이 크기 중 최댓값 -> sum(times)
start, end = max(times), sum(times)

while start <= end:
    mid = (start + end) // 2

    # mid 값을 최적값이라고 가정 (가능한 블루레이의 크기 중 최소)
    # 누적값으로 카운팅
    # 다돌았는데 블루레이 개수가 m개 이하면 최솟값이라 가정하고 범위 좁히기
    total = 0
    count = 1

    for time in times:
        if total + time > mid:
            count += 1
            total = 0
        total += time

    if count <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
