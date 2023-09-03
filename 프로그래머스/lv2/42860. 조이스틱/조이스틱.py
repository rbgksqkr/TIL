def currentMinCount(target):
    start = ord('A')
    end = ord('Z') + 1
    return min(ord(target) - start, end - ord(target))
    
def solution(name):
    answer = 0
    minMove = len(name) - 1
    nextIndex = 0
    while name[minMove] == 'A' and minMove > 0:
        minMove -= 1
        if minMove < 0:
            return answer
    
    for i, target in enumerate(name):
        answer += currentMinCount(target)     
        nextIndex = i + 1
        
        while nextIndex < len(name) and name[nextIndex] == 'A':
            nextIndex += 1
            
        minMove = min(minMove, i + i + len(name) - nextIndex, i+(len(name) - nextIndex)*2)
    answer += minMove
    
    return answer