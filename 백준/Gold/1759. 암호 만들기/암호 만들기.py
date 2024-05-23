# --- 요구사항 분석 ---
# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 암호를 이루는 알파벳이 오름차순
# 문자의 종류는 C가지
# TODO: C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하기

# --- 풀이 방법 ---
# 4 6 // L C
# a t c i s w
# 2번째줄에 들어오는 알파벳을 하나의 배열로 저장하고, 오름차순으로 정렬
# 최소 모음 1개, 자음 2개 사용한 L개의 암호 찾기

import sys
input = sys.stdin.readline
L, C = map(int, input().split())
data = list(input().strip().split())

data.sort()

answer = []
자음_개수 = 0
모음_개수 = 0


def check(x):
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        return True
    return False


def dfs(x):
    global 자음_개수, 모음_개수
    if len(answer) == L and 자음_개수 >= 2 and 모음_개수 >= 1:
        print(''.join(answer))
        return
    for i in range(x, C):
        if data[i] not in answer:
            isValid = check(data[i])
            if isValid:
                모음_개수 += 1
            else:
                자음_개수 += 1
            answer.append(data[i])
            dfs(i + 1)
            answer.pop()
            if isValid:
                모음_개수 -= 1
            else:
                자음_개수 -= 1


dfs(0)
