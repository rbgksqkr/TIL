# 조건 1 : 맨 왼쪽 위는 1,1 (인덱스+1) / 판은 이어붙여짐
# 조건 2 : 비바라기 시전시 (N,1) (N,2) (N-1, 1) (N-1 2)에 비구름 생성
# 조건 3-1 : 구름이 전부 d방향 s칸 이동
# 조건 3-2 : 각 구름 칸 바구니 물 저장양 증가
# 조건 3-3 : 구름 삭제
# 조건 3-4 : 물 양이 증가한 칸에서 물복사 사용해서 대각선 방향 거리 1안에 바구니수 만큼 물 양증가 (경계 넘은거 제외)
# 조건 3-5 : 바구니에 저장된 물의 양이 2 이상이면 모든 칸에 구름이 생기고, 물 양이 줄어듦

import sys
N, M = map(int, sys.stdin.readline().split())
basket = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [9, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [9,-1, -1, 0, 1, 1, 1, 0, -1]
cross = [[-1,-1],[-1,1],[1,-1],[1,1]] #대각선 체크용
cloud = [[N-1,0],[N-2,0],[N-1,1],[N-2,1]] # 조건 2
for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())
    visited = [[0]*N for _ in range(N)]
    clouds = []
    
    while cloud :
        y, x = cloud.pop() # 조건 3-3
        ny, nx = (y + dy[d]*s) % N, (x + dx[d]*s) % N # 조건 1 + 조건 3-1
        basket[ny][nx] += 1
        visited[ny][nx] = 1
        clouds.append([ny,nx])

    for ny, nx in clouds:   
        for ly, lx in cross :
            my, mx = ny + ly, nx + lx
            if 0 <= my < N and 0 <= mx < N and basket[my][mx]: # 조건 3-4 
                basket[ny][nx] += 1

    for i in range (N): # 조건 3-5
        for j in range (N):
            if basket[i][j] >= 2 and not visited[i][j]:
                basket[i][j] -= 2
                cloud.append([i,j])

print(sum(map(sum,basket))) # 전체 합을 구해주자
