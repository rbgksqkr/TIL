def solution(n, arr1, arr2):
    answer = []
    bins = []

    for i, j in zip(arr1, arr2):
        binary = i|j
        bins.append(format(binary, 'b'))

    for i in bins:
        temp = ""
        i = i.zfill(n)
        for j in i:
            if j == '0':
                temp += " "
            if j == '1':
                temp += "#"
        answer.append(temp)
        
    return answer
