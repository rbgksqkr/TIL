def solution(s):
    answer = []
    s = s.lower()
    str_list = s.split(' ') # split() 옵션을 안넣으면 공백많아도 1개로 취급 !
    for i in range(len(str_list)):
        str_list[i] = str_list[i].capitalize()
    return ' '.join(str_list)
