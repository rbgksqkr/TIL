# 수빈이는 점 N. 동생은 점 K.  (0 ≤ N ≤ 100,000) (0 ≤ K ≤ 100,000)
# 수빈이는 걷거나 순간이동 가능
# X일 때 걷는다면 '1초' 후에 X-1 또는 X+1로 이동
# 순간이동을 하는 경우에는 '0초' 후에 2*X의 위치로 이동

# TODO: 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후?

# 1. n, k 를 입력받는다.
# 2. x-1, x+1, 2*x 탐색
# 3. 2*x를 갈 땐 0초인 것을 고려.

import sys
from collections import deque
input = sys.stdin.readline

MAX = 100001

n, k = map(int, input().split())

queue = deque([n])
visited = [0 for _ in range(MAX)]
visited[n] = 1

while queue:
    x = queue.popleft()

    if x == k:
        print(visited[k]-1)
        break

    for i in [x*2]:
        mx = i

        if mx < 0 or mx >= MAX:
            continue

        if not visited[mx]:
            visited[mx] = visited[x]
            queue.append(mx)

    for i in [x-1, x+1]:
        mx = i

        if mx < 0 or mx >= MAX:
            continue

        if not visited[mx]:
            visited[mx] = visited[x] + 1
            queue.append(mx)
