import copy

# cctv 1,2,3,4,5번의 종류별 가능한 방향을 숫자로 나타냄
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def watch(x, y, dir, temp):
    for d in dir:
        mx = x
        my = y
        while True:
            mx += dx[d]
            my += dy[d]

            if mx < 0 or my < 0 or mx >= n or my >= m:
                break
            
            if temp[mx][my] == 6:
                break

            if temp[mx][my] == 0:
                temp[mx][my] = '#'

def dfs(data, cnt):
    global answer

    temp = copy.deepcopy(data)
    if cnt == cctv_cnt:
        c = 0
        for i in temp:
            c += i.count(0)
        answer = min(answer, c)
        return
    number, x, y = cameras[cnt]
    for i in directions[number]:
        watch(x, y, i, temp)
        dfs(temp, cnt + 1)
        temp = copy.deepcopy(data)


n, m = map(int, input().split())
data = []
cameras = []
cctv_cnt = 0
answer = int(1e9)
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(m):
        if 1 <= data[i][j] <= 5:
            cameras.append((data[i][j], i, j))
            cctv_cnt += 1

dfs(data, 0)
print(answer)
