import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

result = 0
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(idx, cnt):
    global result
    visited[idx] = True
    cnt += 1
    
    if  cnt == 5:
        result = 1
        return 
    
    for f in graph[idx]:
        if visited[f] == False:
            visited[f] = True
            dfs(f, cnt)
            
    visited[idx] = False
    
for i in range(n):
    if result == 1 :
        break
    dfs(i, 0)
    
print(result)