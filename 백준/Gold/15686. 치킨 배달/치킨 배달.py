import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
houses = []
chickens = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            houses.append([i, j])
        elif line[j] == 2:
            chickens.append([i, j])
    graph.append(line)

INF = int(1e9)
answer = INF
for chicken in list(combinations(chickens, m)):
    total_min_dist = 0  # 치킨거리의 합
    for house in houses:
        x, y = house
        min_dist = INF  # 특정 집에서 치킨거리
        for i in chicken:
            cx, cy = i
            dist = abs(x-cx) + abs(y-cy)
            min_dist = min(min_dist, dist)
        total_min_dist += min_dist

    # 치킨거리의 합 중 최솟값
    answer = min(answer, total_min_dist)
print(answer)
