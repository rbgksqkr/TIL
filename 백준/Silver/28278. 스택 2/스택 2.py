# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    line = list(map(int, input().split()))
    if len(line) == 2:
        stack.append(line[1])
        continue

    if line[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif line[0] == 3:
        print(len(stack))
    elif line[0] == 4:
        print(1 if not stack else 0)
    elif line[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
