import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]


def isAttachable(sticker, x, y):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if graph[x+i][y+j] == 1 and sticker[i][j] == 1:
                return False
    return True


def attach(sticker, x, y):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            graph[x+i][y+j] += sticker[i][j]


def rotate(sticker):
    r, c = len(sticker), len(sticker[0])
    rotate_sticker = [[0 for _ in range(r)] for _ in range(c)]
    for i in range(c):
        for j in range(r):
            rotate_sticker[i][j] = sticker[r-1-j][i]
    return rotate_sticker


for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    isAttached = False
    for i in range(4):
        r, c = len(sticker), len(sticker[0])
        if isAttached:
            break
        for x in range(n-r+1):
            if isAttached:
                break
            for y in range(m-c+1):
                if isAttachable(sticker, x, y):
                    attach(sticker, x, y)
                    isAttached = True
                    break
        sticker = rotate(sticker)


count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            count += 1
print(count)
