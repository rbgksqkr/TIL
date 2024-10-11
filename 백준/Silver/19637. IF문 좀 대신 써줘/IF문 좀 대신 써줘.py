# --- 문제 분석 ---
# 캐릭터가 가진 전투력을 기준으로 칭호를 붙여주려고 한다.
# 예를 들어,
# 전투력 10,000 이하의 캐릭터는 WEAK,
# 10,000 초과 그리고 100,000 이하의 캐릭터는 NORMAL,
# 100,000 초과 그리고 1,000,000 이하의 캐릭터는 STRONG 칭호

# TODO: 캐릭터의 전투력에 맞는 칭호를 출력하는 프로그램을 작성

# --- 문제 풀이 ---
# 10^5 * 10^5 = 시간 초과
# 10000, 100000, 1000000 을 이진탐색으로 찾기 => n log n
# 최소 인덱스 + 1
# FIXME: target을 구하는 게 아니라 target이 특정 값 이하인지 체크하는 로직을 구현못함


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

mapper = {}
for i in range(n):
    name, standard = input().split()
    mapper[i] = int(standard), name


def binary_search(array, target, start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if array[mid][0] >= target:
            end = mid - 1
            res = mid
        else:
            start = mid + 1
    return array[res][1]


for j in range(m):
    target = int(input())
    result = binary_search(mapper, target, 0, n-1)
    print(result)
