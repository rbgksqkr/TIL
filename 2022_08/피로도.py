from itertools import permutations
def solution(k, dungeons):
    answer = -1
    dun_list = list(permutations(dungeons, len(dungeons)))
    for i in dun_list:
        temp, result = k, 0
        for j in i:
            if temp >= j[0]:
                temp -= j[1]
                result += 1
        if answer < result:
            answer = result
            
    return answer
