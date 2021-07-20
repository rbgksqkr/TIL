def solution(numbers, hand):
    answer = ''
    left, right = (0,0), (2,0)
    left_key = [1, 4, 7]
    right_key = [3, 6, 9]
    # 0~9의 좌표
    location = [(1,0), (0,3), (1,3), (2,3), (0,2), (1,2), (2,2), (0,1), (1,1), (2,1)]
    
    for i in range(len(numbers)):
        if numbers[i] in left_key:
            left = location[numbers[i]]
            answer += "L"
        elif numbers[i] in right_key:
            right = location[numbers[i]]
            answer += "R"
        else:
            l_distance = abs(left[0]-location[numbers[i]][0]) + 
            abs(left[1]-location[numbers[i]][1])
            r_distance = abs(right[0]-location[numbers[i]][0]) + 
            abs(right[1]-location[numbers[i]][1])
            
            if l_distance < r_distance:
                left = location[numbers[i]]
                answer += "L"
            elif l_distance > r_distance:
                right = location[numbers[i]]
                answer += "R"                
            else:
                if hand == "left":
                    left = location[numbers[i]]
                    answer += "L"
                else:
                    right = location[numbers[i]]
                    answer += "R"
        

    
    
    return answer
