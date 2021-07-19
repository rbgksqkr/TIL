def solution(numbers):
    # 가장 큰 수가 나올 수 있는 조합만 구하기
    # 앞자리 수가 큰 순서대로 정렬
    # {앞자리수:원래숫자}
    front = dict()
    str_numbers = list(map(str, numbers)) # 다시 문자열로 변환

    for i in str_numbers:
        front[i] = i[0]

    sorted_numbers = sorted(str_numbers, reverse=True)

    answer = ''.join(sorted_numbers)
