import math
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 원의 중심 사이의 거리를 구하기 -> distance
    distance = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    if distance == 0 and r1 == r2:  # 동심원인데 반지름이 같음 -> 못만남
        print(-1)
    elif distance == r1 + r2 or distance == abs(r1-r2):  # 외접 또는 내접
        print(1)
    elif distance < r1 + r2 and distance > abs(r1 - r2):  # 서로 다른 두점
        print(2)
    else:
        print(0)
