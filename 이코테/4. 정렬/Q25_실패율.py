def solution(N, stages):  #N=5, stages = [2, 1, 2, 6, 2, 4, 3, 3]
    result = []
    users = len(stages) # 스테이지에 도달한 플레이어 수
    stages.sort()
    count_stages = [0 for _ in range(N+1)] # 클리어하지 못한 플레이어의 수
    for i in range(users):
        if stages[i] <= N:
            count_stages[stages[i]] += 1
            
    for i in range(1, N+1):
        count = count_stages[i]
        if users == 0: # 마지막 스테이지까지 클리어 한 사용자가 없는 경우 0으로 나눠서 런타임에러
            fail = 0
        else:
            fail = count / users # 실패율
        result.append((i, fail))
        users -= count
    
    result.sort(key=lambda x:(-x[1], x[0]))
    return [i[0] for i in result]