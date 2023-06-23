import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

targets = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])
count = 0
for target in targets:
    index = queue.index(target)
    n = len(queue)
    dist = 0
    if index == 0:
        queue.popleft()
        continue
    if index <= n // 2:
        dist = index
        queue.rotate(-dist)
    else:
        dist = n - index
        queue.rotate(dist)
    count += dist
    queue.popleft()

print(count)