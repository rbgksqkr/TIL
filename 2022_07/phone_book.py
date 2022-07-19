def solution(phone_book):
    answer = True
    phone_book.sort() # 문자열 정렬의 순서는 숫자 정렬 순서와 다르다 !
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            return answer         
    return answer
