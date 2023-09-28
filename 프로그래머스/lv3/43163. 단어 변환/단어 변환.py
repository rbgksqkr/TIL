count = 0

def solution(begin, target, words):
    n = len(words)
    words.sort()
    if target not in words:
        return 0
    
    visited = [0 for _ in range(n)]
    def dfs(start, target, visited):
        global count
        n = len(words)
        if start == target:
            return True
        for i in range(n):
            # 한글자만 바뀐 것 판단
            flag = 0
            m = len(start)
            for j in range(m):
                if start[j] != words[i][j]:
                    flag += 1
            if flag >= 2:
                continue
            # 방문 판단
            if not visited[i]:
                print(start, words[i])
                visited[i] = 1
                count += 1
                if dfs(words[i], target, visited):
                    return True
        return False
    dfs(begin, target, visited)
        
    return count