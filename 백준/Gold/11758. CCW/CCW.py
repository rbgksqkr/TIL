# P1, P2, P3를 순서대로 이은 선분이 반시계 방향을 나타내면 1, 시계 방향이면 -1, 일직선이면 0을 출력한다.
# 1 1
# 5 5
# 7 3

point = []
for _ in range(3):
    point.append(list(map(int, input().split())))  # 입력 저장

x1, y1 = point[0]
x2, y2 = point[1]
x3, y3 = point[2]


def ccw(x1, x2, x3, y1, y2, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)


result = ccw(x1, x2, x3, y1, y2, y3)

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)
