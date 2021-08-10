def solution(s):
    remainder = s
    temp, idx, count = 0, 0, 0

    while remainder:
        if idx + 1 >= len(s):
            break
        if remainder[temp] != remainder[idx]:
            temp = idx
        elif temp != idx:
            remainder = remainder.replace(remainder[temp]*2, '')
            temp, idx = 0, 0
            continue           
        idx += 1
        
    if remainder:
        return 0
    else:
        return 1
