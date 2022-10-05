N, M = map(int, input().split())
x, y, dir = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

dx = [0, -1, 0, 1] # 북(0) 동(1) 남(2) 서(3) 순서로 바라볼 때 이동할 위치
dy = [-1, 0, 1, 0]

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[x][y] = 1

result = 1
while True:
    temp_x, temp_y = x, y # 이동했는 지 확인하는 변수
    for _ in range(4):
        mx = x + dx[dir]
        my = y + dy[dir]
        
        if mx < 0 or my < 0 or mx >= N or my >= M: # 맵을 벗어나면 continue
            continue
        
        if maps[mx][my] == 0 and visited[mx][my] == 0: # 육지이고 가보지 않았다면 이동
            visited[mx][my] = 1
            x, y = mx, my
            result += 1
            break
        
        if dir == 0:
            dir = 3
        else:
            dir -= 1
            
        print("x, y : ", x, y, ", 북(0) 동(1) 남(2) 서(3) : ", dir, ", 방문한 칸 수 : ", result)
    if temp_x == x and temp_y == y: # 네 방향 모두 가본 칸
        temp_dir = 0
        if dir == 0:
            temp_dir = 3
        else:
            temp_dir = dir - 1
        mx = x + dx[temp_dir]
        my = y + dy[temp_dir]

        if maps[mx][my] == 0: 
            x, y = mx, my
        else: # 한칸 뒤로 가려는데 바다면 game over
            break

print(result)

# 4 4
# 1 1 0
# 1 1 1 1  
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1