import sys
from collections import deque
input = sys.stdin.readline

# 집 -> 타겟 사이의 거리 계산
# 편의점 -> 타겟 사이의 거리 계산
# 집 -> 타겟 사이의 거리 > 편의점 -> 타겟 사이의 거리 : 탐색
#  집 -> 해당 타겟 사이의 거리가 1000 이하인지 계산
# 1000 이하면 이동

def bfs():
    visited = [0 for _ in range(n+1)]
    queue = deque([[home_x, home_y]])

    while queue:
        x, y = queue.popleft()

        if abs(x-target_x) + abs(y-target_y) <= 1000:
            print('happy')
            return

        for i in range(n):  # 편의점들 확인
            if not visited[i]:  # 편의점을 방문하지 않았다면
                new_x, new_y = facilities[i]  # 편의점의 좌표를 새로 뽑고
                if abs(x-new_x) + abs(y-new_y) <= 1000:  # 다음거리까지 갈 수 있다면
                    visited[i] = 1  # 방문체크해주고
                    queue.append((new_x, new_y))  # 큐에 담아준다
    print('sad')
    return


T = int(input())
for _ in range(T):
    n = int(input())
    home_x, home_y = map(int, input().split())
    facilities = [list(map(int, input().split())) for _ in range(n)]
    target_x, target_y = map(int, input().split())
    bfs()
