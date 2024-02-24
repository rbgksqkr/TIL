import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [0 for _ in range(f+1)]

dx = [u, -d]


def bfs():
    queue = deque([s])
    visited[s] = 1
    while queue:
        cur = queue.popleft()
        if cur == g:
            return visited[cur] - 1

        for i in range(2):
            mx = cur + dx[i]
            if (0 < mx <= f) and visited[mx] == 0:
                visited[mx] = visited[cur] + 1
                queue.append(mx)
    if visited[g] == 0:
        return 'use the stairs'


print(bfs())
