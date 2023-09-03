# 위아래 커서 이동 최솟값
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
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        nextIndex = i + 1
        while nextIndex < len(name) and name[nextIndex] == 'A':
            nextIndex += 1
        
        # 왼쪽 오른쪽 커서 이동 최솟값
        # 1. 모든 알파벳 지나가기
        # 2. A가 가장 많이 연속되는 부분의 앞부분을 2번지나기
        # 3. A가 가장 많이 연속되는 부분의 뒷부분을 2번지나기
        minMove = min(minMove, i + i + len(name) - nextIndex, i + (len(name) - nextIndex)*2)
    answer += minMove
    
    return answer