# --- 문제 분석 ---
# 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다
# Ai의 오큰수 : 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
# 그러한 수가 없는 경우에 오큰수는 -1
# TODO:  N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력

# --- 문제 풀이 ---
# 1. N과 수열을 입력받는다.
# 2. 수열의 뒤에서부터 stack에 넣는다.
# 3. 현재 인덱스를 체크할 땐 stack에 오른쪽에 있는데 오른쪽에 있는 순서다. 그래서 뒤에서부터 체크하면 가장 왼쪽에 있는 수

# 1. 7 : len(stack) == 0: -1
# 2. 2 : stack = [7]. stack[-1] > arr[idx]: 7
# 3. 5 : stack = [7, 2]. stack[-1] < arr[idx]: pop. stack[-1] > arr[idx]: 7
# 4. 3 : stack = [7, 5]. stack[-1] > arr[idx]. 5
# answer = [5, 7, 7, -1]

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr = list(reversed(arr))
stack = [arr[0]]
answer = [-1]

for i in range(1, n):
    while stack:
        if stack[-1] > arr[i]:
            answer.append(stack[-1])
            break

        stack.pop()

    if i >= len(answer):
        answer.append(-1)
    stack.append(arr[i])

print(*answer[::-1])
