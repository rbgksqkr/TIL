# --- 요구 사항 ---
# N개의 정점과 M개의 간선으로 구성된 무방향 그래프
# 1번부터 N번
# 모든 간선의 가중치는 1
# 인접 정점은 오름차순으로 방문
# TODO: 정점 R에서 시작하여 dfs로 노드를 방문할 경우 노드의 방문 순서 출력

# --- 풀이 방법 ---
# 간선을 그래프 형태로 저장하고 시작 정점에서부터 dfs로 타고 들어가기
# 시작 정점에서부터 i번째까지의 거리를 dist배열로 관리
# dist배열을 순서대로 출력

import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
n, m, start = map(int, input().split())

dist = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n+1):
    graph[i].sort()


def dfs(x):
    global count
    visited[x] = count

    for i in graph[x]:
        if visited[i]:
            continue
        count += 1
        dfs(i)


count = 1
visited[start] = 1
dfs(start)
for i in range(1, n+1):
    print(visited[i])
