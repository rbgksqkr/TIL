# 차량별로 주차 요금 계산
# 요금표 / 입.출차 기록 / 자동차별 주차요금
# IN -> 객체에 저장. total과 temp 나누기.
# 주차 시간 = 출차한 시각 - 입차한 시각
# if 주차 시간 > fees[0]: dic[차량번호] = math.ceil((주차시간 - fees[0]) / fees[2]) * fess[3]
# if 주차 시간 <= fees[0]: dic[차량번호] = fees[1]

import math

def getMinute(time):
    hour, minute = time.split(':')
    hour, minute = int(hour), int(minute)
    return hour * 60 + minute
    
def solution(fees, records):
    answer = []
    
    parking_record = {}
    total_time = {}
    lastTime = getMinute('23:59')
    
    for record in records:
        time, number, command = record.split()
        
        formatTime = getMinute(time)
        if command == 'IN':
            parking_record[number] = formatTime
        else:
            if total_time.get(number):
                total_time[number] += formatTime - parking_record[number]
            else:
                total_time[number] = formatTime - parking_record[number]
            del parking_record[number]
    
    for key in parking_record.keys(): # 11:59 출차
        if total_time.get(key):
            total_time[key] += lastTime - parking_record[key]
        else:
            total_time[key] = lastTime - parking_record[key]

    # if 주차 시간 > fees[0]: dic[차량번호] = math.ceil((주차시간 - fees[0]) / fees[2]) * fess[3]
    # if 주차 시간 <= fees[0]: dic[차량번호] = fees[1]
    for key in total_time.keys(): # 주차 요금 계산
        if total_time[key] > fees[0]:
            answer.append([key, math.ceil((total_time[key] - fees[0]) / fees[2]) * fees[3] + fees[1]])
        else:
            answer.append([key, fees[1]])
    
    answer.sort()
    
    return [i[1] for i in answer]