import math

def solution(progresses, speeds):

    times = []
    answer = []
    front = 0
    
    for i in range(len(progresses)):
        days = 0
        days = math.ceil((100-progresses[i]) / speeds[i])
        times.append(days)
    print(times)
    
    for idx in range(len(times)):
        if times[idx] > times[front]:  
            answer.append(idx - front)
            front = idx 
    answer.append(len(times) - front) 
    
    return answer
