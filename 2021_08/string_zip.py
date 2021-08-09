def solution(s):
    answer = ""
    count  = 0
    idx = 0
    while True:
        if idx > len(s):
            break
        temp = s[idx]
        for  j in range(len(s)):
            if s[j] != temp:
                answer += str(count)+temp
                idx += count
                count = 0
                break                
            else:
                count += 1                
    
    print(answer)
                
        
