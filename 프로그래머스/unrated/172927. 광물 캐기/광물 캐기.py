# 5개씩 그룹 묶기
# 다이아가 많은 그룹에 다이아 곡갱이 사용
# 내림차순 정렬 후 다이아 -> 철 -> 돌 순서대로 사용
def solution(picks, minerals):
    answer = 0
    total_pick = sum(picks)
    length = len(minerals) // 5 + 1
    storage = [[0, 0, 0] for _ in range(length)]
    
    if total_pick <= length:
        length = total_pick
    
    
    for i in range(length):
        for j in range(5):
            idx = i*5 + j
            if idx >= len(minerals):
                break
            
            if minerals[idx] == 'diamond':
                storage[i][0] += 1
            if minerals[idx] == 'iron':
                storage[i][1] += 1
            if minerals[idx] == 'stone':
                storage[i][2] += 1
    
    storage.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    
    for value in storage:
        dia, iron, stone = value
        for i in range(len(picks)):
            if i == 0 and picks[i] > 0:
                answer += dia + iron + stone
                picks[i] -= 1
                break
            elif i == 1 and picks[i] > 0:
                answer += 5*dia + iron + stone
                picks[i] -= 1
                break
            elif i == 2 and picks[i] > 0:    
                answer += 25*dia + 5*iron + stone
                picks[i] -= 1
                break
    
    return answer