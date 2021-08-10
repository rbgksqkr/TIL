def solution(scores):
    answer = ''
    students = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[]}
    for i in range(len(scores)):
        for j in range(len(scores)):
            students[i].append(scores[j][i])

    for i in range(len(scores)):
        if min(students[i]) == students[i][i] and students[i].count(min(students[i])) == 1:
            students[i].remove(min(students[i]))
        elif max(students[i]) == students[i][i] and students[i].count(max(students[i])) == 1:
            students[i].remove(max(students[i]))

        mean = sum(students[i]) / len(students[i])
        if mean >= 90:
            answer += "A"
        elif mean >= 80:
            answer += "B"
        elif mean >= 70:
            answer += "C"
        elif mean >= 50:
            answer += "D"
        else:
            answer += "F"

    return answer
