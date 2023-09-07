# 최소한의 객실만을 사용
# 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용 가능
# 퇴실 시간 정렬 후 퇴실 제일 빠른 걸 큐에 넣어
# 큐의 처음 퇴실 시간보다 입실 시간이 빠르다 - count + 1
# 큐의 처음 퇴실 시간보다 입실 시간이 10분이상 늦다 - count 유지
def solution(book_time):

    # 풀이설명1 : 함수 만들기
    def change_min(str_time: str) -> int:
        return int(str_time[0:2]) * 60 + int(str_time[3:])
	
    #풀이 설명2 : 예약 시간이 빠른 순으로 정렬하기
    book_times = sorted([[change_min(i[0]), change_min(i[1]) + 10] for i in book_time])
	
    #풀이 설명3 : 방 배정하기
    rooms = []
    for book_time in book_times:
        if not rooms:
            rooms.append(book_time)
            continue
        for index, room in enumerate(rooms):
            if book_time[0] >= room[-1]:
                rooms[index] = room + book_time
                break
        else:
            rooms.append(book_time)
    return len(rooms)