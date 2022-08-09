def solution(brown, yellow):
    answer = []
    length = brown + yellow
    for i in range(3, length//2 + 1):
        if length % i == 0:
            m, n = i, length//i
            if m*2 + (n-2) * 2 == brown:
                answer.append(m)
                answer.append(n)
                break 
    answer.sort(reverse=True)
    return answer
