import heapq
def solution(food_times, k):
    answer = 0
    heap = []
    n = len(food_times)
    for i in range(n):
        heapq.heappush(heap, (food_times[i], i+1))
        
    if sum(food_times) <= k:
        return -1
      
    count = 0
    while (heap[0][0]-count) * len(heap) <= k:
        k -= (heap[0][0]-count) * len(heap)
        count += heap[0][0]-count
        heapq.heappop(heap)
        
    result = sorted(heap, key = lambda x : x[1])    
    answer = result[k % len(heap)][1]    
    return answer
