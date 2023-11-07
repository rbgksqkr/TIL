def solution(routes):
    answer = 1
    n = len(routes)
    cur_idx = 0
    target_idx = 1
    routes.sort(key=lambda x:x[1])
    
    if n == 1:
        return answer
    
    while target_idx < n:
        if routes[cur_idx][1] < routes[target_idx][0]: # 뒤에가 더 크면 나눠
            cur_idx = target_idx
            target_idx += 1
            answer += 1
        else:
            target_idx += 1
    
    return answer