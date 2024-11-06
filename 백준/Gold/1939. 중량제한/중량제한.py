# N개의 섬으로 이루어진 나라. (2 ≤ N ≤ 10,000)
# 몇 개의 섬 사이에는 다리 설치.
# 다리마다 중량제한 존재.
# 서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다.

# TODO: 공장이 위치해 있는 두 섬 사이에서, 한 번의 이동으로 옮길 수 있는 물품들의 중량의 최댓값?
# 1. n(섬), m(다리) 을 입력받는다.
# 2. m개의 줄에 a(출발), b(도착), c(중량제한) 를 입력받는다.
# 3. 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수 입력받는다.
# 4. 입력받은 공장 섬 번호에서 탐색 시작.
# 5. 중량 제한이 최대가 되는 경로 만들기
# 5-2. 중량을 탐색할 때 저장해서 min으로 비교해 경로의 최솟값이 마지막에 위치
# 5-3. 마지막에선 max로 작은 값 중 최댓값 비교

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
start_x, start_y = -1, -1
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

for i in range(1, n+1):
    graph[i].sort(reverse=True)

start, end = list(map(int, input().split()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(mid):
    visited[start] = 1
    queue = deque([start])

    while queue:
        x = queue.popleft()

        if x == end:
            return True

        for mx, mc in graph[x]:
            if not visited[mx] and mid <= mc:
                queue.append(mx)
                visited[mx] = 1

    return False


left, right = 1, 1000000000
while left <= right:
    visited = [0 for _ in range(n+1)]
    mid = (left + right) // 2

    if bfs(mid):  # 목적지까지 도달 가능
        left = mid + 1
    else:
        right = mid - 1
print(right)
