# --- 요구 사항 ---
# ana호가 행성 간 이동을 하는데 걸리는 시간이 2차원 행렬로 주어짐
# graph[i][j] : i 번째 행성에서 j 번째 행성에 도달하는데 걸리는 시간
# TODO: 모든 행성을 탐사하는데 걸리는 최소 시간을 계산

# --- 풀이 방법 ---
# graph[0][2] + graph[2][1]
# 모든 지점에서 모든 지점까지의 최단거리 구하기
# 발사되는 행성 위치에서 모든 지점 최단거리로 순회하기

# 입력
# 3 0
# 0 30 1
# 1 0 29
# 28 1 0

# 출력
# 2

import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

n, start = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

queue = deque([start])
visited = [0 for _ in range(n)]
visited[start] = 1
permutation = list(permutations([i for i in range(n) if i != start], n-1))
answer = int(1e9)
for i in permutation:
    result = 0
    temp = start
    for j in i:
        result += graph[temp][j]
        temp = j
    answer = min(answer, result)
print(answer)
