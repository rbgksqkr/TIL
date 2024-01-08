# '(', ')', '[', ']' 4개의 기호 존재.
# 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.
# ‘()’의 괄호값 2, ‘[]’ 의 괄호값 3이다.
# ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
#  ‘()[[]]’ : ()=2, []=3, [[]]=3*3=9, => 11

import sys
input = sys.stdin.readline

input_data = input().strip()

stack = []
result = 0
last = ''
res = 1
for idx, i in enumerate(input_data):
    if i == '(':
        res *= 2
        stack.append(i)
    elif i == '[':
        res *= 3
        stack.append(i)
    elif i == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if input_data[idx-1] == '(':
            result += res
        res //= 2
        stack.pop()
    elif i == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if input_data[idx-1] == '[':
            result += res
        res //= 3
        stack.pop()
if stack:
    result = 0
print(result)
