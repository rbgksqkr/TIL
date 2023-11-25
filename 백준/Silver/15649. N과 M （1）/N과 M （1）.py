import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

def back():
    # 탈출 조건
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    # 재귀
    for i in range(1, N+1):
        if i not in answer:  # 중복없이
            answer.append(i)
            back()
            answer.pop()

back()