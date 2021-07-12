import math

def solution(progresses, speeds):

    times = []
    distribution = []
    functions = 1
    idx = 0 
    
    for i in range(len(progresses)):
        days = 0
        days = math.ceil((100-progresses[i]) / speeds[i])
        times.append(days)
    print(times)
    
    gap = 1
    for idx, i in enumerate(times):
        
        # print(gap)
        for j in times[gap:len(times)]:
            if i <= j:
                distribution.append(functions)
                print("배포 추가 : i : ",i,"j : ",j)
                gap = idx+functions + 1
                print("idx, functions. gap : ", idx, functions, gap)
                functions = 1
                print("gap : " ,gap)
                break
            functions += 1
            print("시작인덱스", gap, times[idx],"기능 추가 :", functions, "뒤의 기능", j)


            
    
    return distribution
    
