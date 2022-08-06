import heapq
def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [INF for _ in range(N+1)]   
    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2])) 
    
    queue = []
    heapq.heappush(queue,(0, 1))
    distance[1] = 0
    while queue:
        dist, cur = heapq.heappop(queue)
        
        if distance[cur] < dist: # 저장된 거리가 새로운 정보보다 짧을 경우
            continue
        
        for i in graph[cur]:
            cost = dist + i[1]
            
            if distance[i[0]] > cost: # 다른 노드를 거쳐가는 게 거리가 더 짧을 경우
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    
    for i in distance:
        if i <= K:
            answer += 1
        
    return answer
