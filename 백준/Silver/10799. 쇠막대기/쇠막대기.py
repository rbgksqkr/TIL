# 모든 ‘( ) ’는 반드시 레이저를 표현한다.
# 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다.
# stack에 괄호가 남아있는 개수만큼 쇠막대기 존재
# count에 레이저로 잘린 횟수 + 1 개 추가
# stack.append(['(', 0)])
# ')'가 나올때 바로 직전 문자가 '(' 이면 레이저 발사하여 잘린 횟수 +1

import sys
input = sys.stdin.readline

data = list(input().strip())

stack = []
count = 0
for idx, i in enumerate(data):
    if i == '(':
        stack.append([i, 0])
    elif i == ')':
        top = stack.pop()
        if data[idx-1] == '(':
            for j in stack:
                j[1] += 1
        if top[1] > 0:
            count += top[1] + 1
print(count)
