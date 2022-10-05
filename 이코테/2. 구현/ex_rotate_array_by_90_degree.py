# 2차원 리스트를 시계방향으로 90도 회전한 결과를 반환하는 함수
def rotate_array_by_90_degree(array):
    n = len(array) # 행 길이
    m = len(array[0]) # 열 길이
    rotate_array = [[0 for _ in range(n)] for _ in range(m)] # 행과 열이 array와 반대인 리스트
    for i in range(n):
        for j in range(m):
            rotate_array[j][n-i-1] = array[i][j]
    return rotate_array

array = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
result = rotate_array_by_90_degree(array)
print(array)
print(result)