# --- 요구 사항 ---
# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷기 or 순간이동
# X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
# TODO: 수빈이가 동생을 찾을 수 있는 가장 빠른 시간?

# --- 문제 풀이 ---
# 양끝점 고려
# 맨 처음 방문한 게 최단시간이므로 visited 체크하기
# x-1, x+1, 2*x 를 queue에 넣고 bfs 돌리기

import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

dist = [0 for _ in range(100001)]
path = [0 for _ in range(100001)]


def find_path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = path[temp] # 뒤에서부터 순서대로 경로찾기
    print(*arr[::-1])


def bfs():
    queue = deque([[n, 0]])

    while queue:
        x, count = queue.popleft()

        if x == k:
            print(dist[x])
            find_path(x)
            return

        for dx in [x-1, x+1, x*2]:
            mx = dx

            if mx < 0 or mx > 100000:
                continue

            if not dist[mx]:
                dist[mx] = dist[x] + 1  # bfs는 최단거리이므로 최초 방문 시 최단거리
                path[mx] = x  # mx를 가는 경로에 x 지점을 담는다
                queue.append([mx, count+1])


bfs()
