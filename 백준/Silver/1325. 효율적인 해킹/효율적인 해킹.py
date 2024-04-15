# --- 요구사항 ---
# N개의 컴퓨터
# 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹
# 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있음
# A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다
# TODO: 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력

# --- 풀이 방법 ---
# count 세기
# 3 1 -> 3이 1을 신뢰. 1을 해킹하면 3을 해킹할 수 있음
# 3 2 -> 3이 2을 신뢰. 2을 해킹하면 3을 해킹할 수 있음
# 4 3 -> 4이 3을 신뢰. 3을 해킹하면 4을 해킹할 수 있음
# 5 3 -> 5이 3을 신뢰. 3을 해킹하면 5을 해킹할 수 있음
# 1을 해킹하면 1, 3, 4, 5 해킹 가능
# 2를 해킹하면 2, 3, 4, 5 해킹 가능
# graph : [[], [3], [3], [4, 5], [], []]

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)


def bfs(x):
    queue = deque([x])
    visited = [0 for _ in range(n+1)]
    visited[x] = 1
    count = 1
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                count += 1
                queue.append(i)
    return count


answer = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if graph[i]:
        answer[i] = bfs(i)

max_count = max(answer)
for i in range(1, n+1):
    if answer[i] == max_count:
        print(i, end=' ')
