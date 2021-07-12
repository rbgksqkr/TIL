def solution(dartResult):
    answer = []
    idx = 0
    for index, i in enumerate(dartResult): 
                
        if i.isdecimal():
            if i == '0' and dartResult[index-1] == '1':
                    answer[idx-1] = 10
            else:
                answer.append(int(i))
                idx += 1
        elif i == '*':
            if len(answer) == 1:
                answer[idx-1] = answer[idx-1] *2
            else:
                answer[idx-2] = answer[idx-2]*2
                answer[idx-1] = answer[idx-1]*2
        elif i == '#':
            answer[idx-1] = answer[idx-1]*(-1)
        elif i == 'S':
            answer[idx-1] = answer[idx-1]**1
        elif i == 'D':
            answer[idx-1] = answer[idx-1]**2            
        elif i == 'T':
            answer[idx-1] = answer[idx-1]**3
        
    result = sum(answer)
    return result
