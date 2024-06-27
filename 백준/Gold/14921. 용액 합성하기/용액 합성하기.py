# --- 문제 분석 ---
# 각 용액은 -100,000,000부터 100,000,000사이의 특성 값
# 같은 양의 두 용액을 혼합하면, 그 특성값은 두 용액의 특성값의 합
# 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액 제작
# 각 용액은 10ml시험관에 10ml씩 들어있고, 빈 20ml 시험관이 단 하나 있다.
# 게다가 용액을 계량할 수 없어서, 두 용액을 섞을 때는 10ml씩 섞어서 20ml로 만드는데, 단 한번밖에 할 수 없다.

# ex) [-101, -3, -1, 5, 93]
# -101, 93 => -8 용액을 혼합하면 -8인 용액을 만들 수 있다.
# 5, 93 => 98 용액을 혼합하면 특성 값이 98인 용액을 만들 수 있다.
# 모든 가능한 조합을 생각해 보면, 특성값이 2인 용액이 0에 가장 가까운 용액이다.
# 용액들의 특성값 A1, … ,AN이 오름차순 입력값으로 주어짐
# TODO: 두 개의 용액을 혼합하여 만들 수 있는 0에 가장 가까운 특성값 B 출력

# --- 문제 풀이 ---
# 어떤 두 용액을 섞을 것인지 결정
# 2 ≤ N ≤ 100,000. N^2 = 100억 (x)
# 투포인터로 체크
# 0과 가깝다 == 절댓값이 작다
# start와 end를 움직이는 기준이 잘못됨. answer의 절댓값을 기준으로 세웠더니 예외 발생.
# total이 0보다 작으면 end를 줄이고, total이 0보다 크면 start를 늘림

import sys
input = sys.stdin.readline
N = int(input())
liquids = list(map(int, input().split()))

start, end = 0, N-1

answer = int(1e9)
while start < end:
    total = liquids[start] + liquids[end]
    if abs(answer) > abs(total):
        answer = total
    if total < 0:
        start += 1
    else:
        end -= 1

print(answer)
