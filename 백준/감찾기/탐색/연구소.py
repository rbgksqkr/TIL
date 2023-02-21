import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
virus = []
spaces = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 0:
            spaces.append([i, j])
        if line[j] == 2:
            virus.append([i, j])
    graph.append(line)

# 안전영역 최댓값 구하기
# --- 번복 ---
# 벽 3개 세우기 --> 3개를 어떻게 돌려야 전체 경우를 다 돌 수 있을까?
# virus 퍼뜨리기
# 안전영역 구하기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def printGraph(graph):
    for a in range(n):
        for b in range(m):
            print(graph[a][b], end=' ')
        print()
    print()


def getSafeSpace(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count


def spread(newGraph):
    queue = deque(virus)
    global result

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if newGraph[mx][my] == 0:
                newGraph[mx][my] = 2
                queue.append([mx, my])

    result = max(result, getSafeSpace(newGraph))


result = 0
combination_space = list(combinations(spaces, 3))
for k in combination_space:
    graph_copy = copy.deepcopy(graph)
    for i, j in k:
        graph_copy[i][j] = 1
    spread(graph_copy)

print(result)
