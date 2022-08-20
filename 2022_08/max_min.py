def solution(s):
    answer = ''
    int_list = list(map(int, s.split()))
    int_list.sort()
    answer = str(int_list[0]) + " " + str(int_list[-1])
    return answer
