# 택배 크기 동일. 1-n번 상자 오름차순으로 일렬 배열.
# 맨 앞에 놓인 상자 != 트럭에 실어야 하는 순서 -> 보조 컨테이너 벨트 (맨 마지막 추가 상자만 뺄 수 있음)

from collections import deque

def solution(order):
    answer = 0
    
    belt = []
    idx = 0
    for box in range(1, len(order) + 1):
        belt.append(box)
        while (belt) and (belt[-1] == order[idx]):
            answer += 1
            idx += 1
            belt.pop()

    return answer