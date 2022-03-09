import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    queue = []
    for i in range(1, N+1):
        if indegree[i] == 0:
              heapq.heappush(queue, i)

    while queue:
        n = heapq.heappop(queue)
        result.append(n)
        for i in graph[n]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(queue, i)  
    for i in result:
        print(i, end=' ')


topology_sort()
