import heapq
def solution(n, paths, gates, summits):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    # 산봉우리 판별
    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True
        
    heap = []
    
    distance = [INF for _ in range(n+1)]
    for gate in gates:
        heapq.heappush(heap, [0, gate])
        distance[gate] = 0
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist or is_summit[now]:
            continue
            
        
        for next_node, cost in graph[now]:
            cost = max(distance[now], cost)
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(heap, [cost, next_node])
    
    result = [-1, INF]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
    return result
        
    