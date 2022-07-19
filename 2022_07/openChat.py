def solution(record):
    answer = []
    result = []
    relation = {}
    for i in record:
        answer.append(i)
        command = i.split() 
        if command[0] == 'Enter' or command[0] == 'Change':
            relation[command[1]] = command[2]    
    
    for i in answer:
        command = i.split()
        if command[0] == 'Enter':
            result.append(relation[command[1]]+"님이 들어왔습니다.")
        elif command[0] == 'Leave':
            result.append(relation[command[1]]+"님이 나갔습니다.")
    
    return result
