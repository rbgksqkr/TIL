from collections import deque
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

now_x, now_y, now_dir = map(int, input().split())
target_x, target_y, target_dir = map(int, input().split())


def turnLeft(dir):
    if dir == 1:
        dir = 4
    elif dir == 3:
        dir = 1
    elif dir == 2:
        dir = 3
    else:
        dir = 2
    return dir

def turnRight(dir):
    if dir == 1:
        dir = 3
    elif dir == 4:
        dir = 1
    elif dir == 2:
        dir = 4
    else:
        dir = 2
    return dir


dx = [0, 0, 1, -1] # 동 서 남 북 : 1, 2, 3, 4
dy = [1, -1, 0, 0]


def bfs(now_x, now_y, now_dir):
    queue = deque()
    visited = [[[0 for _ in range(5)] for _ in range(m)] for _ in range(n)]
    visited[now_x][now_y][now_dir] = 1
    queue.append((now_x, now_y, now_dir, 0))
    while queue:
        x, y, dir, count = queue.popleft()
        if x == target_x-1 and y == target_y-1 and dir == target_dir:
            return count
        
        for i in range(1, 4):
            mx = x + (dx[dir-1] * i)
            my = y + (dy[dir-1] * i)

            if 0 <= mx < n and 0 <= my < m and data[mx][my] == 0:
                if visited[mx][my][dir] == 0:
                    visited[mx][my][dir] = 1
                    queue.append((mx, my, dir, count+1))
            else:
                break

        # 맵을 벗어나거나 벽인 경우
        left = turnLeft(dir)
        right = turnRight(dir)
        if visited[x][y][left] == 0:
            visited[x][y][left] = 1
            queue.append((x, y, left, count+1))
        if visited[x][y][right] == 0:
            visited[x][y][right] = 1
            queue.append((x, y, right, count+1))

print(bfs(now_x-1, now_y-1, now_dir))
