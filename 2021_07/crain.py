def solution(board, moves):
    bucket = [0]
    answer = 0
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                if board[j][moves[i]-1] == bucket[-1]:
                    bucket.pop(-1)
                    answer += 2
                else:
                    bucket.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break             

    return answer
