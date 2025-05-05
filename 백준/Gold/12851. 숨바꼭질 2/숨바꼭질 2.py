# --- 문제 분석 ---
# N. K. X일 때 1초 후 X-1, X+1, X*2
# TODO: 가장 빠른 시간 + 가장 빠른 시간으로 찾는 방법 개수

# 최단시간은 4로 잘 나왔는데, count가 1이 나온다. why?
# 탐색했을 때 첫번째 나온 케이스가 최단 경로
# 최단 경로로 가는 방법이 여러개라면 모든 탐색을 돌리는 것인가?
# 모든 탐색을 돌리면 시간초과는 안나는가?
# 현재 모든 탐색을 돌렸는데 왜 1가지만 나오는가?

import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)
graph = [-1] * 100001 # 0 <= N, K <= 100000
count = [0] * 100001
N, K = map(int, input().split())

def bfs(x):
    global answer,count
    queue = deque([x])
    graph[x] = 0
    count[x] = 1
    while queue:
        x = queue.popleft()

        for dx in [x-1, x+1, x*2]:
            if dx < 0 or dx > 100000:
                continue

            # print(dx)
            if graph[dx] == -1:
                graph[dx] = graph[x] + 1
                count[dx] = count[x]
                queue.append(dx)
            elif graph[dx] == graph[x] + 1:
                count[dx] += count[x]

bfs(N)
print(graph[K])
print(count[K])