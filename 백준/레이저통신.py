from collections import deque

m, n = map(int, input().split())

data = []
laser = []
for i in range(n):
    data.append(list(input().strip()))
    for j in range(m):
        if data[i][j] == 'C':
            data[i][j] = '.'
            laser.append((i, j))

start_x, start_y = laser[0][0], laser[0][1]
target_x, target_y = laser[1][0], laser[1][1]

dx = [-1, 0, 1, 0] # 북 동 남 서 :  0 1 2 3
dy = [0, 1, 0, -1]



def bfs(x, y):
    queue = deque()
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or my < 0 or mx >= n or my >= m:
            continue

        if data[mx][my] == '.':
            visited[mx][my] = 1
            queue.append((mx, my, i, 0))
    
    while queue:
        x, y, dir, count = queue.popleft()
        if x == target_x and y == target_y:
            return count

        mx = x + dx[dir]
        my = y + dy[dir]
        
        if 0 <= mx < n and 0 <= my < m:
            if data[mx][my] == '.' and visited[mx][my] == 0:
                visited[mx][my] = 1
                queue.append((mx, my, dir, count))
        
        left = turnLeft(dir)
        mx = x + dx[left]
        my = y + dy[left]

        if 0 <= mx < n and 0 <= my < m:
            if data[mx][my] == '.' and visited[mx][my] == 0:
                visited[mx][my] = 1
                queue.append((mx, my, left, count+1))

        right = turnRight(dir)
        mx = x + dx[right]
        my = y + dy[right]

        if 0 <= mx < n and 0 <= my < m:
            if data[mx][my] == '.' and visited[mx][my] == 0:
                visited[mx][my] = 1
                queue.append((mx, my, right, count+1))
    

def turnLeft(dir):
    return (dir-1) % 4


def turnRight(dir):
    return (dir+1) % 4


print(bfs(start_x, start_y))
