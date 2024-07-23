# --- 문제 상황 ---
# 3명으로 구성된 팀만 참가가 가능
# 코딩 실력이 좋으면 팀워크가 떨어지고, 팀워크가 좋을수록 코딩 실력이 떨어진다.
# 모든 학생들의 코딩 실력을 알고 있다.
# 각각의 코딩 실력 Ai는 -10000부터 10000 사이의 정수로 표시되어 있다.
# 세 팀원의 코딩 실력의 합이 0이 되는 팀을 만들고자 한다.
# TODO: 그녀가 대회에 출전할 수 있는 팀을 얼마나 많이 만들 수 있는지를 계산?

# --- 풀이 방법 ---
import sys
input = sys.stdin.readline

N = int(input())
codings = list(map(int, input().split()))

codings.sort()


answer = 0
for i in range(N-2):
    start, end = i+1, N-1
    max_idx = N
    while start < end:
        sumScore = codings[start] + codings[end] + codings[i]

        if sumScore == 0:
            if codings[start] == codings[end]:
                answer += end - start
            else:
                if max_idx > end:
                    max_idx = end
                    while max_idx >= 0 and codings[max_idx - 1] == codings[end]:
                        max_idx -= 1
                answer += end - max_idx + 1

            start += 1
        elif sumScore > 0:
            end -= 1
        elif sumScore < 0:
            start += 1

print(answer)
