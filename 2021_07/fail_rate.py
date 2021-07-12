def solution(N, stages):  
    fail_percent = dict()
    users = len(stages)
    for i in range(1, N+1):
        if users == 0: # 도전자가 0이 되는 경우
            fail_percent[i] = 0
            continue        
        count = stages.count(i)
        fail_percent[i] = count / users
        users -= count

                
    
    new_dic = sorted(fail_percent.items(), key=lambda x:x[1], reverse=True)
    
    return list(dict(new_dic).keys())
