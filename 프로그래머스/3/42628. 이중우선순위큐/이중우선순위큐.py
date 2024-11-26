
# 순간 순간 정렬이 필요하므로 queue로는 해결하기 어렵다.
# heap이라면 한쪽으로만 정렬이 가능한데, 매번 정렬해주고 플래그로 분기처리?
# 최대힙, 최소힙을 따로 관리하면 한 쪽이 비었을 때 분기 처리 어려움 -> 무조건 1개로 관리
# 1개의 힙에서 최댓값 최솟값을 다 뽑을 수 있는가?
import heapq

def solution(operations):
    answer = []
    
    heap = []
    
    for operation in operations:
        oper, num = operation.split()
        num = int(num)
        
        if oper == 'I':
            heapq.heappush(heap, num)
        elif oper == 'D':
            if num == 1 and heap:
                max_num = max(heap)
                heap.remove(max_num)
            elif num == -1 and heap:
                heapq.heappop(heap)
        
    
    if not heap:
        return [0, 0]
    
    return [max(heap), heapq.heappop(heap)]