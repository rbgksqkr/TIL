import re

def solution(new_id):
    answer = new_id.lower()
    
    answer = re.sub("[^-_.a-z0-9]","",answer) # 소문자, 숫자, -, _, .
    answer = re.sub("[.]+", ".",answer) # 2번 이상 연속된 마침표 치환
    answer = re.sub("^[.]|[.]$", "",answer) # 마침표가 맨앞이거나 맨뒤에 있으면 제거
    
    if not answer:
        answer += 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    if len(answer) <= 2:
        while(len(answer) < 3):
            answer += answer[-1]

    return answer
