# 1시간동안 똥꼬쇼해서 풀긴 품
# 시간제한 1초, s의 길이 최대 1000 이므로 O(N^2) 가능
# 자르고 남는 문자열 처리하는 거 구현하는 게 오래걸림
import copy


def solution(s):
    answer = len(s)  # 1000 넘는 임의의 값 초기화 -> 자기자신으로 초기화하고 압축안되면 그대로 return
    for i in range(1, len(s)//2+1):  # 문자열을 i개 단위로 자른다
        result = ''  # 각각의 단위로 자른 결과값 저장
        count = 1  # 단위별 압축 문자열 반복횟수 저장
        pre = s[:i]  # 첫번째 문자열 자르기
        for j in range(i, len(s)+1, i):
            now = s[j:j+i]  # 현재 문자열과 이전 문자열 비교
            if now and len(now) != i:  # 뒷부분에 딱 떨어지지 않는 문자열 저장
                result += now
            if pre == now:  # 문자열이 연속되면 count += 1
                count += 1
            else:  # 문자열이 연속되지 않았을 때
                if count == 1:  # 1개면 그냥 넣고
                    result += pre
                else:
                    result += str(count)+pre  # 1개이상이면 숫자를 붙여서 넣어준다
                pre = now
                count = 1
        answer = min(answer, len(result))  # 가장 짧은 길이로 표현되는 문자열로 갱신
    return answer
