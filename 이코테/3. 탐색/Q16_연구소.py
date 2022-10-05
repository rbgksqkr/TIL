from collections import deque
import copy

# 벽 만들기
# 빈 칸을 벽으로 만들고 count+1을 넣어 재귀적으로 호출한다.
# 벽을 3개를 세웠을 때 bfs()를 실행한다.
def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if labs[i][j] == 0:
                labs[i][j] = 1
                make_wall(count+1)
                labs[i][j] = 0

# 바이러스 퍼뜨리고 안전지역 계산하기
# 벽을 어떻게 세우냐에 따라 바이러스 퍼지는 게 다르기 때문에 그값을 저장하기 위해 임시 리스트를 만든다.
# 바이러스를 퍼뜨린 후 안전 지역을 계산한다.
def bfs():
    queue = deque()
    test_labs = copy.deepcopy(labs)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if labs[i][j] == 2:
                queue.append([i, j])  
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or my < 0 or mx >= n or my >= m:
                continue
            if test_labs[mx][my] == 0:
                test_labs[mx][my] = 2
                queue.append([mx, my])

    global answer
    count = 0
    for i in range(n):
        for j in range(m):
            if test_labs[i][j] == 0:
                count += 1 
    answer = max(answer, count)



n, m = map(int, input().split())
labs = []
for i in range(n):
    labs.append(list(map(int, input().split())))

answer = 0
make_wall(0)
print(answer)