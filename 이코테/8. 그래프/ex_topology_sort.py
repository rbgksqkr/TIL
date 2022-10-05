########### 위상정렬 알고리즘 #############
# 1. 인접리스트 방식으로 그래프를 저장한다.
# 2. 저장할 때 진입차수를 따로 계산해서 저장한다.
# 2-1. 각 노드로 진입하는 간선 개수 == 진입차수
# 3. 진입차수가 0인 노드부터 큐에 넣고 반복문을 돈다.
# 4. 3번에서 구한 노드와 연결된 노드들과의 간선을 끊으면서 진입차수를 1 감소한다.
# 5. 이때 연결된 노드들 중 진입차수가 0이 된 노드를 큐에 넣는다.
# 6. 진입차수가 0이 된 순서가 정렬 순서다.
#######################################

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v+1)

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    global indegree
    result = []
    queue = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end = ' ')

topology_sort()