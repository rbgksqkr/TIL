from collections import deque
import sys
input = sys.stdin.readline


def bfs(now_z, now_x, now_y):
    dx = [-1, 1, 0, 0, 0, 0] # 북 남 서 동 상 하
    dy = [0 ,0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1] 

    queue = deque()

    queue.append((now_z, now_x, now_y, 0))

    while queue:
        z, x, y, count = queue.popleft() 


        for i in range(6):
            mx = x + dx[i]
            my = y + dy[i]
            mz = z + dz[i]

            if (0 <= mx < r and 0 <= my < c and 0 <= mz < l):
                if data[mz][mx][my] == 'E':
                    return count+1
                if data[mz][mx][my] == '.' and visited[mz][mx][my] == 0:
                    visited[mz][mx][my] = 1
                    queue.append((mz, mx, my, count+1))


while True:
    l, r, c = map(int, input().split()) # 층 수, 행, 열

    if (l, r, c) == (0, 0, 0):
        break

    data = [[[]*c for _ in range(r)] for _ in range(l)]

    for i in range(l):
        data[i] = [list(input().strip()) for _ in range(r)]
        input()

    now_z, now_x, now_y = 0, 0, 0

    for k in range(l):
        for i in range(r):
            for j in range(c):
                if data[k][i][j] == 'S':
                    now_x, now_y, now_z = i, j, k

    visited = [[[0]*c for _ in range(r)] for _ in range(l)]
    visited[now_z][now_x][now_y] = 1
    result = bfs(now_z, now_x, now_y)
    if result == None:
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(s).')
