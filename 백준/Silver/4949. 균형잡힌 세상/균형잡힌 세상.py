# '(' 또는 '[' 가 나오면 push
# '(' 가 나왔는데 stack 최상단이 ')' 이면 pop, 아니면 no
# '[' 가 나왔는데 stack 최상단이 ']' 이면 pop, 아니면 no
# 다 읽었는데 stack에 괄호가 남아있으면 no

import sys
input = sys.stdin.readline

data = []
while True:
    input_data = input()
    new_str = input_data.replace("\n", "")
    if new_str == '.':
        break
    data.append(new_str)

for i in range(len(data)):
    stack = []
    isValid = True
    for idx, j in enumerate(data[i]):
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0 or stack[-1] != '(':
                isValid = False
                break
            stack.pop()
        elif j == ']':
            if len(stack) == 0 or stack[-1] != '[':
                isValid = False
                break
            stack.pop()

    if len(stack) > 0:
        isValid = False
    if isValid:
        print('yes')
    else:
        print('no')
