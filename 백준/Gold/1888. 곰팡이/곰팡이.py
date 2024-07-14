# --- 요구 사항 ---
# 곰팡이들은 현재 여러 개의 덩어리를 이루고 있는 상태
# m행 n열. 한 칸 당 한 개의 곰팡이. 곰팡이의 덩어리 : 격자 상에 가로세로로 인접한 곰팡이들의 집합
# 맨 처음 상태에서는 한 덩어리 안의 곰팡이들이 모두 같은 종으로, 자라는 속도도 같다.
# 서로 다른 덩어리에 속한 곰팡이는 종이 달라 자라는 속도도 다를 수 있다.
#   시간이 지남에 따라 서로 다른 종의 곰팡이 덩어리가 한 덩어리로 합쳐지는 경우도 있을 수 있다.
#   만약 어느 곰팡이의 자라는 속도가 k라면, 하루가 지났을 때 그 곰팡이가 피어있던 자리를 중심으로 2k+1행 2k+1열의 격자에 같은 종의 곰팡이가 번진다는 의미이다.
#   만약 서로 다른 종의 곰팡이가 같은 칸에 번져 오면, 자라는 속도가 빠른 곰팡이가 그 칸을 차지한다.

# TODO: 곰팡이들이 점점 자라나서 한 덩어리로 될 때까지 시간?

# --- 풀이 방법 ---
# 1. 곰팡이들을 한번에 퍼뜨리기 위해 모든 곰팡이를 queue에 넣는다.
# 2. 자라는 속도가 빠른 곰팡이를 먼저 퍼뜨린다.
# 3. 곰팡이 중심으로 상하좌우 k만큼 격자를 자신으로 채운다.
# 4. k가 2라면, 곰팡이 중심으로 2만큼 떨어진 모든 격자를 채운다.
# FIXME: 한 번 퍼지는 건 성공했는데, 2번째 돌 때의 무한루프

from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


h, w = map(int, input().split())
arr = [list(map(int, input())) for _ in range(h)]
dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def inside(x, y): return 0 <= x < w and 0 <= y < h


def bfs(x, y):  # 곰팡이 덩어리 BFS
    visit[y][x] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in dire:
            nx, ny = x+dx, y+dy
            if inside(nx, ny) and not visit[ny][nx] and arr[ny][nx]:
                visit[ny][nx] = True
                q.append((nx, ny))


def check():  # 곰팡이 덩어리 개수 세는 함수
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visit[i][j]:
                bfs(j, i)
                cnt += 1
    return cnt


def spread():
    narr = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            speed = arr[y][x]
            narr[y][x] = max(narr[y][x], arr[y][x])
            if speed:
                for nx in range(x-speed, x+speed+1):
                    for ny in range(y-speed, y+speed+1):
                        if inside(nx, ny) and arr[ny][nx] < arr[y][x]:
                            narr[ny][nx] = max(narr[ny][nx], arr[y][x])
    return narr


day = 0
visit = [[False]*w for _ in range(h)]
count = check()
while count > 1:
    visit = [[False]*w for _ in range(h)]
    arr = spread()
    count = check()
    day += 1
print(day)
