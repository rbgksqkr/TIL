import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for i in range(M):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)-1):
        start, end = temp[j], temp[j+1]
        graph[start].append(end)
        indegree[end] += 1


def topology_sort():
    queue = deque()
    result = []
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        n = queue.popleft()
        result.append(n)
        for i in graph[n]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
                
    if len(result) == N:
        for i in result:
            print(i)
    else:
        print(0)
        
topology_sort()
