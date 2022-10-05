n = int(input())
directions = list(input().split())
x, y = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for direction in directions:
    mx, my = x, y
    if direction == 'U':
        mx = x + dx[0]
        my = y + dy[0]
    elif direction == 'D':
        mx = x + dx[1]
        my = y + dy[1]
    elif direction == 'L':
        mx = x + dx[2]
        my = y + dy[2]
    elif direction == 'R':
        mx = x + dx[3]
        my = y + dy[3]
    
    if mx >= 0 and my >= 0 and mx <= n and my <= n:
        x, y = mx, my

print(x+1, y+1)
        