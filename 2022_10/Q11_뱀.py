from collections import deque

n = int(input())  # 보드 크기
k = int(input())  # 사과 개수

maps = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    maps[a-1][b-1] = 1

l = int(input())  # 뱀의 방향 변환 횟수
directions = deque()
for _ in range(l):
    x, c = input().split()
    directions.append((int(x), c))
now_x, now_y = 0, 0
maps[now_x][now_y] = 2
snakes = deque([(now_x, now_y)])
snake_length = 1
snake_dir = 1  # 0, 1, 2, 3 : 북쪽부터 시계방향
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북쪽부터 시계방향
answer = 0
x, c = directions.popleft()
while True:
    # 방향 전환 정보 갱신
    if answer == x:
        if c == 'L':
            if snake_dir == 0:
                snake_dir = 3
            else:
                snake_dir -= 1
        else:
            if snake_dir == 3:
                snake_dir = 0
            else:
                snake_dir += 1

        if directions:
            x, c = directions.popleft()
    answer += 1
    dx, dy = now_x+dir[snake_dir][0], now_y+dir[snake_dir][1]
    if dx < 0 or dy < 0 or dx >= n or dy >= n or maps[dx][dy] == 2:  # 게임 끝
        break

    if maps[dx][dy] == 0:  # 사과가 없으면 몸길이 줄이기
        i, j = snakes.popleft()
        maps[i][j] = 0

    maps[dx][dy] = 2
    snakes.append((dx, dy))
    now_x, now_y = dx, dy

print(answer)
