import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

data = [i for i in range(1, n+1)]

queue = deque(data)

while queue:
    cur = queue.popleft()
    if len(queue) == 0:
        print(cur)
        break
    queue.rotate(-1)
