# TODO: 택배 화물이 각 집하장들 사이를 오갈 때 어떤 경로를 거칠지 정해서, 이를 경로표로 정리하는 것
# 간선이 있다 == 두 집하장간에 화물 이동 가능
# 가중치 : 이동에 걸리는 시간
# 경로표 : 한 집하장에서 다른 집하장으로 최단경로로 화물을 이동시키기 위해 가장 먼저 거쳐야 하는 집하장을 나타낸 것
# --- 풀이 방법 ---
# 모든 지점에서 모든 지점까지의 최단 거리를 구해야 함 -> 플로이드
# 최단거리를 비교할 배열 따로, 결과 배열 따로 만들어야 할듯
# 플로이드를 구하려면 인접 리스트 형태로 들어오는 걸 인접 행렬로 변환해야함
# [i][k] + [k][j] < [i][j]: dp[i][j] = dp[i][k] + dp[i][j] -> 이때의 k값을 [i][j]에 저장
# 입력
# 6 10 : 정점 6개, 간선 10개
# 1 2 2 -> 1에서 2 가는 데 2시간 걸림

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
result = [[INF for _ in range(n+1)] for _ in range(n+1)]
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    dist[u][v] = w
    dist[v][u] = w
    result[u][v] = v
    result[v][u] = u

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if dist[i][k] + dist[k][j] < dist[i][j]:
                # result[i][j] = k # 2번 이상 거치면 마지막 거친 곳을 저장하게 됨 -> 첫번째를 저장해야됨
                result[i][j] = result[i][k]  # k로 가기 위한 첫 번째 집하장을 저장
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if result[i][j] == INF:
            print('-', end=' ')
        else:
            print(result[i][j], end=' ')
    print()
