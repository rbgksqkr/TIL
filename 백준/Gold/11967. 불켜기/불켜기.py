import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 1

def switch(r, c):
    global cnt

    for r, c in arr[r][c]:
        if on[r][c]:    # 아직 불이 켜지지 않았다면
            on[r][c] = False    #불을 킨다.
            cnt += 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:   # 이미 방문한 곳이라면,
                    queue.append((r, c))
                    visit[r][c] = False
                    break


N, M = map(int, input().split()) # N: 가로, 세로 M: 스위치 개수

visit = [[True] * N for _ in range(N)]
on = [[True] * N for _ in range(N)]

arr = [[[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    r, c, x, y = map(int, input().split())
    arr[r - 1][c - 1].append((x - 1, y - 1))

queue = [(0, 0)]
visit[0][0] = False # 방문했음
on[0][0] = False    # 스위치 켜졌음


while queue:
    r, c = queue.pop(0)
    switch(r, c)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] and not on[nr][nc]:    #방문한 적도 없고, 불이 켜져있는 곳이라면
            queue.append((nr, nc))
            visit[nr][nc] = False

print(cnt)