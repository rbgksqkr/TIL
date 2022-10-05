from collections import deque
import copy

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
times = [0 for _ in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    times[i] = temp[0]
    for j in range(1, len(temp)-1):
        graph[temp[j]].append(i)
        indegree[i] += 1


def topology_sort():
    result = copy.deepcopy(times)
    queue = deque()

    for i in range(n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now]+times[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)
            

    for i in range(1, n+1):
        print(result[i])


topology_sort()



# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1