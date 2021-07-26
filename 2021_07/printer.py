from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)

    while priorities:
        left = priorities.popleft()
        if [i for i in priorities if left < i]: # 첫번째 문서보다 중요도 높은 문서가 있는 경우
            location -= 1
            priorities.append(left)
            if location < 0:
                location = len(priorities) - 1                
            continue
        
        else: # 중요도가 가장 높은 문서일 경우
            if location == 0: # 원하는 문서일 경우
                answer += 1
                break
            else: # 원하지 않는 문서일 경우
                answer += 1
                location -= 1    
    
    return answer
