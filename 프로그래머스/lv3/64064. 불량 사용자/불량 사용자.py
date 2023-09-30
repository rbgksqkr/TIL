from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = 0
    combi_list = list(permutations(user_id, len(banned_id)))
    
    result = []
    for combi in combi_list:
        if not check(combi, banned_id):
            continue
            
        else:
            combi = set(combi)
            if combi not in result:
                result.append(combi)
    return len(result)