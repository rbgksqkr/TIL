def solution(numbers, hand):
    # 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand
    # 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return
    answer = ''
    left, right = 10, 12
    
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            left = numbers[i]
            answer += "L"
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            right = numbers[i]
            answer += "R"
        # 가운데 2,5,8,0 누를 경우 가까운 손가락 / 거리가 같으면 주손가락
        # 거리를 어떻게 구할거냐? 그냥 빼는건 손가락이 가운데 있을 경우 오류 발생
        else: 
            if abs(left-numbers[i]) > abs(right-numbers[i]):
                right = numbers[i]
                answer += "R"
            elif abs(left-numbers[i]) < abs(right-numbers[i]):
                left = numbers[i]
                answer += "L"                
            if abs(left-numbers[i]) == abs(right-numbers[i]):
                if hand == "left":
                    left = numbers[i]
                    answer += "L"            
                else:
                    right = numbers[i]
                    answer += "R"                    
        
    print(answer)
    
    
    return answer
