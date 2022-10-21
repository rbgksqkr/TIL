n, m = map(int, input().split())

now_x, now_y, dir = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# dir : 0, 1, 2, 3 북쪽부터 시계방향

answer = 1

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

def turn(dir): # 왼쪽으로 회전
    return (dir-1) % 4


while True:
    flag = 0
    data[now_x][now_y] = 2 # 현재 위치 청소
    for i in range(4):
        dir = turn(dir)
        mx = now_x + dx[dir]
        my = now_y + dy[dir]

        if mx < 0 or my < 0 or mx >= n or my >= m:
            continue

        if data[mx][my] == 0:
            answer += 1
            now_x, now_y = mx, my
            flag = 1
            break
    
    if flag == 0: # 네 방향 다 막히거나 청소함
        temp = (dir+2) % 4 # 뒤로 돌기
        if data[now_x+dx[temp]][now_y+dy[temp]] == 2: # 후진
            now_x, now_y = now_x+dx[temp], now_y+dy[temp]
        else:
            break
        
print(answer)
