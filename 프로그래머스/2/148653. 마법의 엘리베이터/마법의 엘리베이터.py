# 절댓값이 10^c 인 버튼
# 위치: 현재 층 수 + 버튼 값
# 위치 <= 0: 이동 x
# 버튼 한 번당 마법의 돌 한 개를 사용
# TODO: 0층으로 가는데 필요한 마법의 돌 최소 개수

# 각 자릿수가 0에 가깝게 이동하는 방향으로 계산
# + 할지, - 할지를 결정해야함
# 2554
# 두번째 자릿수가 방향을 정함.
def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 현재 자릿수가 5일 경우, 다음 자릿수 확인
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer