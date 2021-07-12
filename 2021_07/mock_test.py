def solution(answers):
    first_member = [1,2,3,4,5] # 5번마다 반복
    second_member = [2,1,2,3,2,4,2,5] # 8번마다 반복
    third_member = [3,3,1,1,2,2,4,4,5,5] # 10번마다 반복

    answer_member = {1:0, 2:0, 3:0}
    idx = 0

    for i in answers:
        if i == first_member[idx % 5]:
            answer_member[1] += 1
        if i == second_member[idx % 8]:  
            answer_member[2] += 1
        if i == third_member[idx % 10]:
            answer_member[3] += 1
        idx += 1

    return [k for k, v in answer_member.items() if max(answer_member.values()) == v]
