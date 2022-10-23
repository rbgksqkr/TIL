import copy
n, m = map(int, input().split())

data = []
ice = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(m):
        if data[i][j] != 0:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global temp_ice
    cnt = 0
    visited[x][y] = 1
    temp_ice.append((x, y))
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if data[mx][my] == 0:
            cnt += 1
            
        if data[mx][my] != 0 and visited[mx][my] == 0:
            dfs(mx, my, count+1)
    temp[x][y] = cnt


answer = 0
while True:
    temp = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    temp_ice = []
    
    for i, j in ice:
        dfs(i, j, 1)
        break

    if len(ice) != len(temp_ice):
        break
 
    del_list = []
    for i in range(n):
        for j in range(m):
            if data[i][j] > 0:
                data[i][j] -= temp[i][j]
                if data[i][j] <= 0:
                    data[i][j] = 0
                    del_list.append((i,j))
    ice = list(set(ice)-set(del_list))
    answer += 1


print(answer)
