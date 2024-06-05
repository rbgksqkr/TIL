# 크레딧 C를 받았으며 두 개의 품목을 구매
# 사용 가능한 모든 품목의 목록 L
# 전체 크레딧 가치에 해당하는 두 가지 품목을 구매
# 목록에 있는 항목의 위치를 ​​나타내는 두 개의 정수로 구성 (작은 숫자부터 시작).


# 테스트 케이스 N
# C : amount of credit
# I : the number of items
# P : 각각의 아이템은 아이템의 가격을 나타냄

# 몇 개의 아이템으로 C 가격를 맞출 수 있는지?


import sys
input = sys.stdin.readline

T = int(input())


for k in range(1, T+1):
    C = int(input())
    I = int(input())
    prices = list(map(int, input().split()))
    for i in range(I):
        for j in range(i, I):
            if i == j:
                continue

            result = prices[i] + prices[j]
            if result == C:
                if i > j:
                    i, j = j, i
                print(f'Case #{k}:', i+1, j+1)
                break
