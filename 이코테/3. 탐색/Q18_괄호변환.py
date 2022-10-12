def balanceParen(p):
    left = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            left -= 1
        
        if left == 0:
            return i
    return 0

def properParen(p):
    left = 0
    for i in p:
        if i == '(':
            left += 1
        else:
            if left == 0:
                return False
            left -= 1
    return True
        
def solution(p):
    answer = ''
    if p == '':
        return answer
    idx = balanceParen(p)
    u, v = p[:idx+1], p[idx+1:]
    if properParen(u):
        answer += u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        
        u = u[1:-1]
        
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer
