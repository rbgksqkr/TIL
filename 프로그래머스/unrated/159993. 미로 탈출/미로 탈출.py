# 통로로만 지나갈 수 있다
# 시작 지점 -> 레버 -> 출구
# 시작지점->레버 최소시간 + 레버->출구 최소시간
from collections import deque

def bfs(start, maps, target):
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([[start[0], start[1], 0]])
    
    while queue:
        x, y, count = queue.popleft()
    
        if maps[x][y] == target:
            return count
            
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue

            if not visited[mx][my] and not maps[mx][my] == 'X':
                visited[mx][my] = 1
                queue.append([mx, my, count+1])
                
def solution(maps):
    n, m = len(maps), len(maps[0])
    start = []
    lever = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = [i, j]
            if maps[i][j] == 'L':
                lever = [i, j]
                
    distanceStoL = bfs(start, maps, 'L')
    distanceLtoE = bfs(lever, maps, 'E')

    if distanceStoL == None or distanceLtoE == None:
        return -1
    else: return distanceStoL + distanceLtoE