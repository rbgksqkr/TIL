import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
orders = list(map(int, input().split()))  # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

dice = [0 for _ in range(6)]

dx = [0, 0, 0, -1, 1]  # 동서북남
dy = [0, 1, -1, 0, 0]

for order in orders:
    mx = x + dx[order]
    my = y + dy[order]

    if mx < 0 or my < 0 or mx >= n or my >= m:
        continue

    east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if order == 1:
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif order == 2:
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif order == 3:
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    elif order == 4:
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north

    if graph[mx][my] == 0:
        graph[mx][my] = dice[5]
    else:
        dice[5] = graph[mx][my]
        graph[mx][my] = 0

    x, y = mx, my
    print(dice[4])