import math
from itertools import combinations  

def solution(nums):
    answer = 0
    numbers = list(combinations(nums, 3))
    for i in numbers:
        target = sum(i)
        for j in range(2, int(math.sqrt(target)) + 1):
            if target % j == 0:
                break
            elif j == int(math.sqrt(target)):
                answer += 1        
            
    return answer  
