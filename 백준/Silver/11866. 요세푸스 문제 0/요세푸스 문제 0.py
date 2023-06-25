import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])

answer = []
for i in range(n):
    # if len(queue) >= k:
    # queue.rotate(-(k-1))
    for j in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print('<', end='')
for i in range(n-1):
    print(answer[i], end=', ')
print(f'{answer[-1]}>', end='')
