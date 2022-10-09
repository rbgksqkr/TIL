from itertools import combinations
n, m = map(int, input().split()) # n : 도시 크기,  m: 최대 치킨집 개수

chickens = []
houses = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            chickens.append((i+1, j+1))
        if temp[j] == 1:
            houses.append((i+1, j+1))

total_dist = int(1e9) # 도시의 치킨거리 최솟값
for chicken in combinations(chickens, m): # 폐업시키지 않을 치킨집 M개 고르기
    temp_dist = 0 # 각 상황별 도시의 치킨거리
    for house in houses: # 집을 기준으로
        min_dist = 2*n
        for x, y in chicken: # 가장 가까운 치킨집 찾기
            dist = abs(x-house[0]) + abs(y-house[1])
            min_dist = min(min_dist, dist) # 치킨거리
        temp_dist += min_dist
    total_dist = min(total_dist, temp_dist)

print(total_dist)
