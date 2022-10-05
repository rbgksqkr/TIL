from audioop import getsample
import sys
from turtle import st
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())


start = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중 가장 최단거리가 짧은 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = 1
    for i in graph[start]:
        distance[i[0]] = i[1] # start와 연결된 노드들을 최단거리 테이블에 초기화
    
    for i in range(n-1):
        now = get_smallest_node() # 현재 최단거리가 가장 짧은 노드 찾기
        visited[now] = 1
        for j in graph[now]: # 현재 노드와 연결된 노드들
            cost = distance[now] + j[1] 

            if cost < distance[j[0]]: # 현재 노드를 거쳐 다른 노드로 가는 거리가 더 짧은 경우
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2