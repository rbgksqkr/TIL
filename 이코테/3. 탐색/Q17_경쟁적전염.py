# 바이러스 위치 저장방식을 이차원배열로 저장했더니 꺼낼때도 이중for문을 돌아야되서 시간초과가 났다.
# 배열에 저장하는 방식에 따라 시간복잡도가 달라질 수 있다 !

import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())

maps = []
virus = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            virus.append((temp[j], 0, i, j))
    maps.append(temp)

target_s, target_x, target_y = map(int, input().split())

virus.sort()

queue = deque(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    vi, s, x, y = queue.popleft()

    if s == target_s: # 정해진 시간까지 돌리기
        break

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or my < 0 or mx >= n or my >= n:
            continue

        if maps[mx][my] == 0:
            maps[mx][my] = vi
            queue.append((vi, s+1, mx, my))


print(maps[target_x-1][target_y-1])

# s * k  * virus[i] * 4 = 1000 * 10000
