# 1, 2, 3, 4, 5 순서대로 받을 수 있도록 처리
# ex) 5 4 1 3 2
# stack = [5, 4] 1
# stack = [5, 4, 3] 2
# stack = [5, 4] 3
# stack = [5] 4
# stack = [] 5
# 받으면 Nice, 못받으면 Sad 출력

# order 변수 필요
# order가 아닌 값이 오면 stack에 넣기
# stack 최상단과 line 맨앞이 order이 없으면 stack에 넣어.
# line이 비었는데 stack 최상단이 order가 아니면 실패

import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

stack = []
order = 1
isValid = True

idx = 0
while order <= n:
    if idx < n and line[idx] == order: # 올바른 순서
        order += 1
        idx += 1
        continue
    
    if len(stack) > 0 and stack[-1] == order: # stack에서 꺼냄
        stack.pop()
        order += 1
        continue

    if idx < n: # 줄이 있으면 stack에 넣기
        stack.append(line[idx])
        idx += 1
        continue

    isValid = False
    break

if isValid:
    print("Nice")
else:
    print("Sad")