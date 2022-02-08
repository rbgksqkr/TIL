import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R):
  board.append(input().strip())

graph = [[1 for _ in range(C)] for _ in range(R)]  
visited = [[0 for _ in range(C)] for _ in range(R)]
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]


def bfs(x, y):
  queue = deque([[x,y,board[x][y]]])
  visited[x][y] = 1
  answer = ""
  while queue:
    x, y, char = queue.popleft()
    # if char in answer:
    #   continue

    if board[x][y] not in answer:
      answer += char
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= R or dy >= C:
        continue

      if visited[dx][dy] == 0:
        visited[dx][dy] = 1
        queue.append([dx, dy, board[dx][dy]])

        # graph[dx][dy] = max(graph[dx][dy], graph[x][y] + 1)

      print(queue, answer)

  
bfs(0, 0)
