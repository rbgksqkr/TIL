import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for _ in range(R):
  graph.append(input().strip())


def bfs():
  count = 0
  queue = set()
  queue.add((0, 0, graph[0][0]))
  while queue:
    x, y, alpha = queue.pop()
    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]
    end = alpha
    for i in range(4):
      dx = x + mx[i]
      dy = y + my[i]

      if dx < 0 or dy < 0 or dx >= R or dy >= C:
        continue   
      if graph[dx][dy] in alpha:
        continue
      else:
        end = alpha+graph[dx][dy]
        queue.add((dx, dy, end))
    
    if alpha == end:
      count = max(count, len(alpha))
  
  return count


print(bfs())
