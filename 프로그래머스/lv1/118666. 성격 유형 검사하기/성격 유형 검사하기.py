def solution(survey, choices):
    answer = ''
    total = {"R":0, "T": 0, "C":0, "F": 0, "J":0, "M": 0, "A":0, "N": 0}
    
    for idx, question in enumerate(survey):
        currentChoice = choices[idx]
        if currentChoice == 1 or currentChoice == 7:
            score = 3
            if currentChoice > 4:
                total[question[1]] += score
            else:
                total[question[0]] += score
        if currentChoice == 2 or currentChoice == 6:
            score = 2
            if currentChoice > 4:
                total[question[1]] += score
            else:
                total[question[0]] += score
        if currentChoice == 3 or currentChoice == 5:
            score = 1
            if currentChoice > 4:
                total[question[1]] += score
            else:
                total[question[0]] += score    
    total_list = list(total.items())
    for i in range(0, len(total_list), 2):
        if total_list[i][1] >= total_list[i+1][1]:
            answer += total_list[i][0]
        else:
            answer += total_list[i+1][0]
          
    return answer