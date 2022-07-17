def solution(id_list, report, k):
    answer = {i:[] for i in id_list}
    result = {i:0 for i in id_list}
    report = set(report) # 중복 제거
    report = list(report)
    for i in report:
        a, b = i.split()
        answer[b].append(a) # [신고당한 사람 : [신고한 사람들]]
         
    for i, sirens in answer.items():
        if len(sirens) >= k: # k명 이상에게 신고 받으면
            for j in sirens:
                result[j] += 1

    return list(result.values())
