# 본인이 볼 수 있는 옥상의 수가 아니라, '본인을 볼 수 있는 관리인의 수'
import sys
input = sys.stdin.readline

N = int(input())
height = [int(input()) for _ in range(N)]

stack = []
answer = 0

for cur in height:  # 10 3 7 4 12 2
    while stack and stack[-1] <= cur: # 작거나 같으면 나(빌딩)를 못봄
        stack.pop()  # 옥상을 볼 수 없는 관리인은 전부 제거

    answer += len(stack)  # 옥상을 볼 수 있는 관리인 수
    stack.append(cur)  # 현 빌딩을 스택에 추가

print(answer)
