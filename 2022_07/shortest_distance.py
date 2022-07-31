from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([[0,0]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue
            else:
                if maps[mx][my] == 1:
                    if maps[mx][my] < maps[x][y] + 1:
                        maps[mx][my] = maps[x][y] + 1
                    queue.append([mx, my])
    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]
