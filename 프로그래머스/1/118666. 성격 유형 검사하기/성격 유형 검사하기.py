def solution(survey, choices):
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''
    for i in range(len(choices)):
        right = 0
        if choices[i] > 4:
            right = 1
        test = list(survey[i])
        point = abs(4-choices[i])
        scores[test[right]] += point
        
    if scores['R'] >= scores['T']: answer += 'R'
    else: answer += 'T'
    if scores['C'] >= scores['F']: answer += 'C'
    else: answer += 'F'
    if scores['J'] >= scores['M']: answer += 'J'
    else: answer += 'M'
    if scores['A'] >= scores['N']: answer += 'A'
    else: answer += 'N' 
    
    return answer