def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    l_lost = len(lost)
    for i in lost:
        if i in reserve: # 여벌 체육복 있는 학생이 도난
            l_lost -= 1
            reserve.remove(i)
        elif i-1 in reserve:
            if i-1 not in lost:
                l_lost -= 1
                reserve.remove(i-1)
        elif i+1 in reserve:
            if i+1 not in lost:
                l_lost -= 1
                reserve.remove(i+1)
    return n-l_lost
