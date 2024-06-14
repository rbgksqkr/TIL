# --- 요구 사항 ---
# N×N인 격자. A[r][c] : (r, c)에 있는 모래 양
# 격자의 가운데 칸부터 토네이도의 이동이 시작. 토네이도는 한 번에 한 칸 이동.
# 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동
# 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다.
# α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다.
# 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다.
# 위의 그림은 토네이도가 왼쪽으로 이동할 때이고, 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전하면 된다.

# 토네이도는 (1, 1)까지 이동한 뒤 소멸한다. 모래가 격자의 밖으로 이동할 수도 있다.
# TODO: 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.

# --- 풀이 방법 ---
# 1. x에서 y로 갈 때 흩어지는 모래 비율 구하기
# 2. 4방향으로 회전한 격자 비율 구하기
# 3. 토네이도가 퍼져나가는 방향으로 이동하면서 모래 흩어지게 하기
# 4. 토네이도가 이동할 때마다 격자 밖으로 나간 모래의 양을 누적해서 마지막에 출력

import sys
input = sys.stdin.readline

# 모래 계산하는 함수


def recount(time, dx, dy, direction):
    global answer, start_x, start_y

    # y좌표 계산 & x좌표 갱신
    for _ in range(time):
        start_x += dx
        start_y += dy
        if start_y < 0:  # 범위 밖이면 stop
            break

        # 3. a, out_sand
        total = 0  # a 구하기 위한 변수
        for dx, dy, z in direction:
            nx = start_x + dx
            ny = start_y + dy
            if z == 0:  # a(나머지)
                new_sand = boards[start_x][start_y] - total
            else:  # 비율
                new_sand = int(boards[start_x][start_y] * z)
                total += new_sand

            if 0 <= nx < n and 0 <= ny < n:   # 인덱스 범위이면 값 갱신
                boards[nx][ny] += new_sand
            else:  # 범위 밖이면 answer 카운트
                answer += new_sand


n = int(input())
boards = [list(map(int, input().split())) for _ in range(n)]

answer = 0  # 밖으로 밀려난 모래 양
start_x, start_y = n // 2, n//2  # 가운데

# 2. 방향별 모래 비율 위치
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
        (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]


# 1.토네이도 회전 방향(y위치)
for i in range(1, n + 1):
    if i % 2:
        recount(i, 0, -1, left)
        recount(i, 1, 0, down)
    else:
        recount(i, 0, 1, right)
        recount(i, -1, 0, up)

print(answer)
