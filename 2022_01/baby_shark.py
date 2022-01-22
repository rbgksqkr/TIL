import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []                                                    # 공간 상태
cur_x, cur_y = 0, 0                                           # 상어 위치
fishes = 0                                                    # 총 물고기 개수
size = 2                                                      # 상어 크기
eat = 0                                                       # 상어가 먹은 물고기 개수
times = 0                                                     # 걸린 시간
for i in range(N):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    if temp[j] == 9:                                          # 상어 현재 위치 찾기
      cur_x, cur_y = i, j    
    elif temp[j] != 0:                                        # 물고기 개수 세기 
      fishes += 1
  graph.append(temp)


def bfs(x, y):
  queue = deque([[x, y, 0]])
  fish_list = []                                              # 찾은 물고기 담는 리스트
  visited = [[0 for _ in range(N)] for _ in range(N)]         # 방문 리스트
  visited[x][y] = 1
  graph[x][y] = 0
  min_dist = N*N

  mx = [-1, 1, 0, 0]
  my = [0, 0, -1, 1]
  while queue:
    x, y, dist = queue.popleft()
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= N or dy >= N:              # 그래프 밖을 탐색할 때
        continue
      if not visited[dx][dy]:                                 # 방문하지 않은 그래프 중
        if graph[dx][dy] <= size:                               # 방문할 수 있는 장소일 때
          visited[dx][dy] = 1                                     # 방문처리하고
          if 0 < graph[dx][dy] < size:                            # 물고기를 찾았을 때
            min_dist = dist                                         # 그 물고기와의 거리를 최단거리로 하고
            fish_list.append([dx, dy, dist+1])                      # 물고기 위치와 거리를 fish_list에 삽입
          if dist < min_dist:                                     # 물고기를 아직 못찾았을 때
            queue.append([dx, dy, dist+1])                          # 경로에 추가

  if fish_list:                                               # 모든 그래프를 돌고 나서 물고기가 있으면
    fish_list.sort(key=lambda x:(x[2], x[0], x[1]))             # 거리, 세로, 가로 오름차순으로 정렬
    return fish_list[0]                                         # 최단거리 물고기의 x, y, 거리 return
  else:
    return []
  

while fishes:                                                 # 물고기가 아직 있으면
  answer = bfs(cur_x, cur_y)                                  # 물고기를 찾는다 : bfs 실행횟수 == 물고기 수
  if not answer:                                              # 물고기가 그래프에 원래 없는 경우
    break
  else:                                                       # 물고기를 찾으면
    cur_x, cur_y = answer[0], answer[1]                         # 현재 위치 update
    fishes -= 1                                                 # 물고기 개수 감소
    times += answer[2]                                          # 걸린시간 더해주기
    eat += 1                                                    # 1마리 먹음
    if size == eat:                                             # 크기만큼 물고기를 먹었을 때 size up
      size += 1
      eat = 0
    graph[cur_x][cur_y] = 0                                     # 물고기 먹은 위치 빈 공간으로 만들기

print(times)
