# A, E, I, O, U 만을 사용한 길이 5 이하의 모든 단어 존재

# TODO: 주어진 단어가 사전에서 몇 번째 단어인가?

# 1. AEI -> A -> AA -> AE

# A -> 1
# A ... U 추가 -> 5
# AA ... UU 추가 -> 25
# AAA ... UUU 추가 -> 125
# AAAA ... UUUU 추가 -> 625
# -> 781

# Ixxxx


from itertools import product

def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U']
    for i in range(1,6):
        for per in product(li,repeat = i): # 중복 허용
            answer.append(''.join(per))
    answer.sort()
    return answer.index(word)+1