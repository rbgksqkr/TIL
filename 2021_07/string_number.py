def solution(s):
    answer = ""
    temp = ""
    words = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 
    'six':6, 'seven':7, 'eight':8, 'nine':9}
    for i in s:
        if i.isalpha():
            temp += i
        elif i.isdigit():
            answer += i
            continue
        if temp in words:
                answer += str(words[temp])
                temp = ""
    return int(answer)
