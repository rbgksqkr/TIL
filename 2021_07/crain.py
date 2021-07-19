def solution(board, moves):
    bucket = [0]
    answer = 0
    for i in moves:
        for j in board:
            if i == 1:
                if j[0] != 0:
                    if j[0] == bucket[-1]:
                        bucket.remove(bucket[-1])
                        answer += 2
                    else:
                        bucket.append(j[0])
                    j[0] = 0
                    break
            elif i == 2:
                if j[1] != 0:
                    if j[1] == bucket[-1]:
                        bucket.remove(bucket[-1])
                        answer += 2
                    else:
                        bucket.append(j[1])
                    j[1] = 0
                    break
            elif i == 3:
                if j[2] != 0:
                    if j[2] == bucket[-1]:
                        bucket.remove(bucket[-1])
                        answer += 2
                    else:
                        bucket.append(j[2])
                    j[2] = 0
                    break
            elif i == 4:
                if j[3] != 0:
                    if j[3] == bucket[-1]:
                        bucket.remove(bucket[-1])
                        answer += 2
                    else:
                        bucket.append(j[3])
                    j[3] = 0
                    break
            elif i == 5:
                if j[4] != 0:
                    if j[4] == bucket[-1]:
                        bucket.remove(bucket[-1])
                        answer += 2
                    else:
                        bucket.append(j[4])
                    j[4] = 0
                    break


    return answer
