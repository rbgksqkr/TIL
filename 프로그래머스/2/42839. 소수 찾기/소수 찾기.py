# 문자열 숫자를 한자리 숫자로 쪼개 만들 수 있는 소수 개수?

# 1. 반복문 돌아서 흩어진 종이 조각으로 만들 수 있는 모든 수를 구한다.
# 2. 구한 수 중 소수인 것을 카운팅한다.

from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(pow(num, 0.5))+1):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = []
    numbers = list(numbers)
    arr = []
    for i in range(1, len(numbers)+1):
        arr += list(permutations(numbers, i))
    num = [int(''.join(t)) for t in arr]    
    
    for i in num:
        if isPrime(i):
            answer.append(i)
    
    return len(set(answer))
