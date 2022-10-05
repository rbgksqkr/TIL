def balance_paren(p):
    left = 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            left -= 1
        
        if left == 0:
            return i    
        
def proper_paren(u):
    left = 0
    for i in range(len(u)):
        if u[i] == '(':
            left += 1
        else:
            left -= 1       
        
        if left < 0:
            return False
        
        if left == 0:
            return True
    return False
        
def solution(p):
    result = ''
    if p == '': # 1단계 : 빈 문자열
        return result
    idx = balance_paren(p) # 2단계 : 균형잡힌 문자열
    u, v = p[:idx+1], p[idx+1:]
    if proper_paren(u): # 3단계 : 올바른 문자열
        result = u + solution(v)
    else: # 4단계 : 올바르지 않은 문자열
        result += '('
        result += solution(v)
        result += ')'
        temp = u[1:-1]
        for i in temp:
            if i == '(':
                result += ')'
            else:
                result += '('
    return result
        