import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
start = int(input())

graph = [[] for _ in range(m+1)]
distance = [INF for _ in range(n+1)]


for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# graph, distance, graph 연결 // visited는 선형탐색할 때 최단거리가 가장 짧은 노드를 선택할 때 필요했다.
################## 기본 세팅 ######################


def dijksttra(start):
    distance[start] = 0
    heap = []

    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist: # 직진하는 것보다 거쳐서 더 빠른 길이 이미 있는 상태
            continue
            
        
        for i in graph[now]: # 현재 노드와 연결된 다른 노드를 돌아
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드를 거쳐가는 게 더 빠른 경우
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    

dijksttra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])




    
