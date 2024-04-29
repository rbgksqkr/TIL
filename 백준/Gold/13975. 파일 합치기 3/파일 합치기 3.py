# --- 요구 사항 ---
# 두 개의 파일을 합쳐서 하나의 임시파일을 만들고,
# 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 파일을 합쳐나가고, 최종적으로는 하나의 파일로 합친다.
# 두 개의 파일을 합칠 때 필요한 비용(시간 등) => 두 파일 크기의 합
# TODO: 최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합?

# --- 풀이 방법 ---
# 40 30 30 50
# 30 + 30 = 60
# 40 + 50 = 90
# 60 + 90 = 150
# 300

import sys
import heapq
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    heap = []
    for i in arr:
        heapq.heappush(heap, i)

    answer = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        total = first + second
        answer += total
        heapq.heappush(heap, total)
    print(answer)
