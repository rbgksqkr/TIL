# --- 문제 분석 ---
# 캠릿브지 대학의 연결구과 : 글자 배열 중요 X -> 양 끝의 글자가 올바른지만 중요하다는 이론
#   즉 단어의 글자가 섞이더라도 '양 끝의 글자만 그대로라면' 원래의 단어를 쉽게 유추하여 이해할 수 있다

# "durumari"와 같은 단어를 "daumurri"로 바꾸게 된다면 원래의 단어를 유추하기 어려움
# 위의 이론이 잘 작동할 수 있는 조건 찾음
#  - 한 단어를 재배열해 다른 단어를 만들 수 있어야 한다.
#  - 두 단어의 첫 글자와 마지막 글자는 서로 동일해야 한다.
#  - 각 단어에서 모음(a, e, i, o, u)을 제거한 문자열은 동일해야 한다.
# 기령이는 새로운 조건을 발견하게 해준 단어를 기려 이를 '두라무리 효과'라 부르기로 했다.

# TODO: 두 단어가 두라무리 효과를 발생시키는지 판별하기

# --- 문제 풀이 ---
# 1. 단어 길이 N 입력 받기
# 2. 2개의 단어 입력받기
# 3. 조건 만족하기
# - 한 단어를 재배열해 다른 단어를 만들 수 있어야 한다.
# - 두 단어의 첫 글자와 마지막 글자는 서로 동일해야 한다.
# - 각 단어에서 모음(a, e, i, o, u)을 제거한 문자열은 동일해야 한다.

import sys
input = sys.stdin.readline

N = int(input())
first = input().strip()
second = input().strip()
vowels = ['a', 'e', 'i', 'o', 'u']


def isEqualFirstEnd():
    return first[0] == second[0] and first[-1] == second[-1]


def isArrange():
    return sorted(first) == sorted(second)


def isExcept():
    new_s1 = new_s2 = ''
    vowel = 'aeiou'
    for i in first:
        if i not in vowel:
            new_s1 += i
    for i in second:
        if i not in vowel:
            new_s2 += i
    if new_s1 == new_s2:
        return True
    else:
        return False


if isEqualFirstEnd() and isArrange() and isExcept():
    print('YES')
else:
    print('NO')
