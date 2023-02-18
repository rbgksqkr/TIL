import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
INF = int(1e9)
times = [INF for _ in range(100001)]
times[n] = 0
queue = deque([[n, 0]])
while queue:
    x, t = queue.popleft()
    if x == k:
        print(t)
        break
    dx = [x*2, x-1, x+1]

    for i in range(3):
        if 0 <= dx[i] <= 100000 and times[dx[i]] > t+1:
            times[dx[i]] = t+1
            queue.append([dx[i], t+1])
