from collections import deque
def solution(number, k):
    number = deque(list(number))
    result = []
    result.append(number.popleft())
    while number and k > 0:
        if not result:
            result.append(number.popleft())
        if result[-1] < number[0]: # 큰 숫자가 앞에 있어야 전체 수가 커진다
            result.pop()
            k -= 1
        else:
            result.append(number.popleft())
    if k > 0: # k가 남은 경우 결과값은 가장 큰 수이므로 뒷자리부터 k개 제거
        return ''.join(result[:-k])
    return ''.join(result+list(number))
    
