def solution(n, words):
    remainder = [words[0]]
    temp = words[0]
    for i in range(1, len(words)):  
        if words[i] in remainder or temp[-1] != words[i][0]:
            order = i // n + 1
            person = i % n + 1
            return [person, order]
        else:
            remainder.append(words[i])
        temp = words[i]

    return [0,0]
