# 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물 수 있는지를 나타냅니다. 
# 지도의 'X'는 바다를 나타내며, 숫자는 무인도
import sys

sys.setrecursionlimit(100000)
count = 0

def dfs(x, y, maps):
    global count
    n, m = len(maps), len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if maps[x][y] != 'X':
        count += int(maps[x][y])
        maps[x][y] = 'X'
        for i in range(4):
            dfs(x+dx[i], y+dy[i], maps)
        return True
    
def solution(maps):
    answer = []
    global count
    convert = []

    n, m = len(maps), len(maps[0])
    for i in maps:
        convert.append(list(i))
    
    for i in range(n):
        for j in range(m):
            if dfs(i, j, convert):
                answer.append(count)
                count = 0
    answer.sort()
    if len(answer):
        return answer
    else:
        return [-1]

