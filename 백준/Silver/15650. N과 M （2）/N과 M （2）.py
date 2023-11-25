import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = []


def back():
    # 2. 오름차순
    # 2가 answer에 있는 상태에서 1이 들어오면 return
    if len(answer) > 1 and answer[-1] < answer[-2]:
        return

    # 탈출 조건
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    # 재귀 조건
    # 1. 중복 X
    for i in range(1, N+1):
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()


back()