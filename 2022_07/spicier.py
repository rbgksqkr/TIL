import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K: # 섞을 때마다 최솟값이 바뀌기 떄문에 heapq 사용
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville) 
        result = first + (second * 2) 
        heapq.heappush(scoville, result)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer
