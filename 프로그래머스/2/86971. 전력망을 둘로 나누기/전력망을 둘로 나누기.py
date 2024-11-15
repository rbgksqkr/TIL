# 2 <= n <= 100.
# 정점(n), 간선 정보(wires) 제공
# 현재의 전력망 네트워크를 2개로 분할

# TODO: 전선들 중 하나를 끊어서 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값) 구하기

# 1. 인접 리스트 형태로 간선들을 저장한다.
# 2. 전선을 하나 끊는다.
# 2-1. 전선에 연결된 송전탑 개수를 구한다.
# 2-2. 전체(n)에서 전선에 연결된 송전탑 개수를 빼 전선에 연결되지 않은 개수를 구한다.
# 3. 2-1과 2-2의 차로 전선을 끊었을 때 두 전력망의 송전탑 개수 차이를 계산한다.
# 4. 두 그래프의 개수 차이가 최솟값을 구한다.
from collections import deque

def check(start, end, visited, graph):
    visited[start] = 1
    visited[end] = 1
    queue = deque([end])
    
    count = 1
    while queue:
        x = queue.popleft()
        
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                count += 1
                queue.append(i)
        
    return count
        
def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n+1)]
    
    # 1. 인접 리스트 형태로 간선들을 저장한다.
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
        
    answer = n
    for wire in wires:
        visited = [0 for _ in range(n+1)]
        a, b = wire
        
        # 2-1. 전선에 연결된 송전탑 개수를 구한다.
        res = check(a, b, visited, graph) # [a, b] 에 연결된 송전탑 개수
        
        # 2-2. 전체(n)에서 전선에 연결된 송전탑 개수를 빼 전선에 연결되지 않은 개수를 구한다.
        alpha = abs(n - res) # [a, b] 에 연결 안된 송전탑 개수 
        
        # 3. 2-1과 2-2의 차로 전선을 끊었을 때 두 전력망의 송전탑 개수 차이를 계산한다.
        result = abs(res - alpha)
        
        # 4. 두 그래프의 개수 차이가 최솟값을 구한다.
        answer = min(answer, result)
    
    return answer