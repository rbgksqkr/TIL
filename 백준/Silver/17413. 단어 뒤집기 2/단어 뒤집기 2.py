from collections import deque
import sys
input = sys.stdin.readline

s = input().strip()
arr = list(s)
queue = deque()
isParen = False
result = ''

for i in arr:
    if i == '<':
        isParen = True
        while queue:
            result += queue.pop()
    queue.append(i)

    if i == '>':
        while queue:
            result += queue.popleft()
        isParen = False

    if i == ' ' and not isParen:
        queue.pop()
        while queue:
            result += queue.pop()
        result += ' '

if queue:
    while queue:
        result += queue.pop()

print(result)
