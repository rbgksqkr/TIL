def solution(plans):
    answer = []
    rest_assignment = []
    plans.sort(key=lambda x:x[1])
    plans_length = len(plans)
    for i in range(1, plans_length):
        prev_hour, prev_minute = map(int, plans[i-1][1].split(':'))
        last_hour, last_minute = map(int, plans[i][1].split(':'))
        diff_hour = last_hour - prev_hour
        diff_minute = last_minute - prev_minute
        
        if diff_hour > 0: diff_minute += diff_hour * 60
        rest_time = int(plans[i-1][2]) - diff_minute
        
        if rest_time > 0:
            rest_assignment.append([plans[i-1][0],rest_time])
            
        if rest_time <= 0:
            answer.append(plans[i-1][0])
            # plans 중간에 시간이 남을 때
            while len(rest_assignment) > 0:
                rest_assignment[-1][1] -= abs(rest_time)
                if rest_assignment[-1][1] <= 0: 
                    rest_time = abs(rest_assignment[-1][1])
                    answer.append(rest_assignment.pop()[0])
                else:
                    break
        
    answer.append(plans[-1][0])
    
    # TODO: plans 끝나고 최근 목록부터 처리
    while len(rest_assignment) > 0:
        answer.append(rest_assignment.pop()[0])
    return answer