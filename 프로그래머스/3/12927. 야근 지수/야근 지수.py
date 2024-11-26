# 1 <= works.length <= 20000. 1 <= n <= 1000000

# 야근 피로도: 야근 시작 시점에서 남은 일의 작업량을 제곱하여 더한 값
# N시간 동안 야근 피로도 최소화
# 1시간 동안 작업량 1만큼 처리.
# TODO: 야근 피로도 최솟값

# 높은 수에서 빼야됨 -> 하나만 낮추는게 아니라 평균적으로 다 낮아야됨
# 기준을 어떻게 계산하는가? (works[i]에서 얼마를 빼야 하는가?)

# 이분탐색: n 이상으로 처리 가능한가?
# left = 0, right: max(works)
# mid가 기준점. works[i] > mid: works[i] - mid; n -= mid

# FIXME: 가장 큰 놈을 빼는 건 맞는데 풀이 방식이 틀림: 이분탐색x -> 최대힙o
# 매번 최댓값을 구할 경우 시간 초과
# 매번 정렬하지 않고 어떻게 최댓값을 구할 수 있을까? -> heap
# 기본값은 최소힙이므로 최대힙을 만들어야함
import heapq

def solution(n, works):
    answer = 0
    
    if n >= sum(works):
        return 0
    
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
    
    for i in range(n):
        data = -heapq.heappop(heap)
        data -= 1
        heapq.heappush(heap, -data)
    
    for i in range(len(heap)):
        answer += heap[i] ** 2
    
    return answer