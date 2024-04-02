# 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 선물을 가장 많이 받을 친구가 받을 선물의 수 ?

# 두 사람이 선물을 주고받은 기록이 있다 -> 이번달까지 더 많은 선물을 준 사람이 다음 달에 선물 받기
# 두 사람이 선물을 주고받은 기록이 없다 or 같다 -> 선물 지수가 더 큰 사람이 받기
# 선물 지수도 같다 -> 다음달에 선물 주고받기 X
# 선물 지수 : 이번 달까지 친구들에게 준 선물의 수 - 받은 선물의 수

# arr[i][j] => { i번째 친구가 j번째 친구에게 준 선물, i번째 친구가 j번째 친구에게 받은 선물 }
# arr =  [..., {give : 0, receive : 1}]
# answer = {a: 0, b: 0}
# --- 

# if arr[i][j][give] != 0 or arr[i][j][receive] != 0 -> 기록 있다
    # if arr[i][j][give] == arr[i][j][receive] -> 같다
        # i의 선믈 지수 : present_i = arr[i][j][give] - arr[i][j][receive]
        # j의 선믈 지수 : present_j = arr[j][i][give] - arr[j][i][receive]
            # if 선물지수 같다 present_i > present_j: answer[i] += 1
            # else if 선물지수 같다 present_i < present_j: answer[j] += 1
    # else
    # -> 선물 준 개수 비교 : arr[i][j][give] >  arr[j][i][give] : answer[i] += 1
    # -> 선물 준 개수 비교 : arr[i][j][give] <  arr[j][i][give] : answer[j] += 1
    
# else -> 기록 없다
# i의 선믈 지수 : present_i = arr[i][j][give] - arr[i][j][receive]
# j의 선믈 지수 : present_j = arr[j][i][give] - arr[j][i][receive]
    # if 선물지수 같다 present_i > present_j: answer[i] += 1
    # else if 선물지수 같다 present_i < present_j: answer[j] += 1

# ---
# if arr[i][j][give] == 0 and arr[i][j][receive] == 0 -> 기록 없다
# else -> 기록 있다
    # if arr[i][j][give] == arr[i][j][receive] -> 같다
    # else
    # -> 선물 준 개수 비교 : arr[i][j][give] >  arr[j][i][give] : answer[i] += 1

def solution(friends, gifts):
    answer = {}
    indexFormat = {} # {'muzi': 0}
    friendFormat = {} # {0: 'muzi'}
    presentPoint = {} # {'muzi': 0}
    
    n = len(friends)
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    for idx, friend in enumerate(friends):
        answer[friend] = 0
        indexFormat[friend] = idx
        friendFormat[idx] = friend
        presentPoint[friend] = 0
        
    for gift in gifts:
        giver, receiver = gift.split(' ')
        arr[indexFormat[giver]][indexFormat[receiver]] += 1
        presentPoint[giver] += 1
        presentPoint[receiver] -= 1
        
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 or arr[j][i] != 0: # -> 기록 있다
                if arr[i][j] != arr[j][i]:
                    if arr[i][j] > arr[j][i]: # i가 더 많이 줌
                        answer[friendFormat[i]] += 1
                    # elif arr[i][j] < arr[j][i]: # j가 더 많이 줌
                    #     answer[friendFormat[j]] += 1
                else:     
                    present_i = presentPoint[friendFormat[i]]
                    present_j = presentPoint[friendFormat[j]]
                    if present_i > present_j: 
                          answer[friendFormat[i]] += 1
            else:
                present_i = presentPoint[friendFormat[i]]
                present_j = presentPoint[friendFormat[j]]
                if present_i > present_j: 
                    answer[friendFormat[i]] += 1
    return max(answer.values())
