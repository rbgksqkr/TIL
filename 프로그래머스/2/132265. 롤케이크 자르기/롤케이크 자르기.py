# 롤케이크의 크기보다 토핑 종류가 중요
# 각 조각에 동일한 가짓수의 토핑 = 공평 (크기, 개수 상관x)
# 100만. <= nlngn
# TODO: 롤케이크를 공평하게 자르는 방법의 수?

# 순회하면서 2개로 나누고, 토핑 가짓수 확인
# 순회하면서 slice할 경우 시간초과
# 
from collections import Counter

def solution(topping):
    left = Counter(topping)
    right = set()

    answer = 0
    for i in topping:
        left[i] -= 1 # 순회하면서 토핑을 1개씩 right으로 추가
        right.add(i)
    
        if left[i] == 0: # 0개가 되면 없애기
            left.pop(i)
            
        if len(left) == len(right):
            answer += 1
    return answer
