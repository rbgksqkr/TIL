def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    k = len(arr2[0])
    answer = [[0]*k for _ in range(n)]
    for i in range(n): 
        lists = []
        for j in range(len(arr2[0])): 
            for k in range(m): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer