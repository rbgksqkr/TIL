# 수빈이는 현재 점 N에 있고, 동생은 점 K에 있다. (0 ≤ N ≤ 100,000) (0 ≤ K ≤ 100,000)
# 걷기 / 순간이동.
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# TODO: 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지?

# 1. -1, 1, 2*x 탐색
# 2. 이동할 때 초를 세기 위해 visited[mx][my] = visited[x][y] + 1

import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())


queue = deque([n])
visited = [0 for _ in range(10**5+1)]


while queue:
    x = queue.popleft()

    if x == k:
        print(visited[k])
        break

    for i in [x-1, x+1, x*2]:
        mx = i

        if mx < 0 or mx > 10**5:
            continue

        if not visited[mx]:
            visited[mx] = visited[x] + 1
            queue.append(mx)
