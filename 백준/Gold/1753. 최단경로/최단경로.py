import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

INF = int(1e9)
distance = [INF for _ in range(v+1)]
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# graph, distance, graph 연결

################## 기본 세팅 ######################

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)

        # 직진하는 것보다 거쳐서 더 빠른 길이 이미 있는 상태
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 노드를 돌아
        for i in graph[now]:
            next_node, cost = i[0], i[1]
            # 다른 노드를 거쳐가는 게 더 빠른 경우
            if dist + cost < distance[next_node]:
                distance[next_node] = distance[now] + cost
                heapq.heappush(queue, (distance[next_node], next_node))


dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
