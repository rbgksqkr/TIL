import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

# (dx, dy): 오른쪽, 아래, 우하, 우상 4방향만 보면 충분
dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

for i in range(19):
    for j in range(19):
        color = board[i][j]
        if color == 0:
            continue

        for dx, dy in dirs:
            # 시작점 강제: 이전 칸이 같은 색이면 시작점 아님
            px, py = i - dx, j - dy
            if in_range(px, py) and board[px][py] == color:
                continue

            # 연속 5개 확인
            ok = True
            for k in range(1, 5):
                nx, ny = i + dx * k, j + dy * k
                if not in_range(nx, ny) or board[nx][ny] != color:
                    ok = False
                    break
            if not ok:
                continue

            # 6번째 방지: 다음 칸이 같은 색이면 6목 이상
            nx, ny = i + dx * 5, j + dy * 5
            if in_range(nx, ny) and board[nx][ny] == color:
                continue

            print(color)
            print(i + 1, j + 1)
            sys.exit()

print(0)
