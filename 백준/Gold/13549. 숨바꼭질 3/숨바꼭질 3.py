from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
dp = [INF for _ in range(100001)]
n, k = map(int, input().split())
dp[n] = 0

queue = deque([n])
visited = [0 for _ in range(100001)]
visited[n] = 1

while queue:
    cur = queue.popleft()
    if cur == k:
        print(dp[k])
        break
    for i in [cur * 2, cur-1, cur+1]:
        if i < 0 or i > 100000 or visited[i]:
            continue
        if i == cur * 2:
            dp[i] = dp[cur]
            visited[i] = 1
            queue.appendleft(i)
        else:
            dp[i] = dp[cur] + 1
            visited[i] = 1
            queue.append(i)
