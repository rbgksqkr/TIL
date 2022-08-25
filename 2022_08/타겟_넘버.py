from collections import deque
def solution(numbers, target):
    answer = 0
    result = deque([numbers[0], -numbers[0]])
    
    for i in range(1, len(numbers)):
        for j in range(len(result)):
            temp = result.popleft()
            temp_list = (temp+numbers[i], temp-numbers[i])
            result += temp_list
            
    for i in result:
        if i == target:
            answer += 1
            
    return answer
