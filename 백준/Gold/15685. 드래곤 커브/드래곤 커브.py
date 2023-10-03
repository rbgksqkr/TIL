import sys
import copy
from collections import deque
input = sys.stdin.readline

N = int(input())
curves = deque()
for _ in range(N):
  curves.append(list(map(int, input().split())))

graph = [[0 for _ in range(101)] for _ in range(101)]

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# temp 에는 이번 세대에서 움직인 방향
# move_array 는 주어진 데이터에서 시작점에서 움직인 방향 모두 저장
while curves:
  y, x, d, g = curves.popleft()
  graph[y][x] = 1
  move_array = [d] # 메모리
  for i in range(g):  
    # queue = [] # 캐싱
    temp = []
    for j in range(len(move_array)):
        temp.append((move_array[j] + 1) % 4)
    temp.reverse()
    move_array += temp

  for i in move_array:
    mx = x + dx[i]
    my = y + dy[i]
    x, y = mx, my
    graph[y][x] = 1

answer = 0
n = len(graph)
m = len(graph[0])
for i in range(100):
  for j in range(100):
      if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
        answer += 1
print(answer)