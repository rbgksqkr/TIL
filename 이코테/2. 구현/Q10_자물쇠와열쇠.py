def rotate_array_by_90_degree(array): # 2차원 리스트 시계방향으로 90도 돌리기
    n = len(array)  # 행 길이
    m = len(array[0])  # 열 길이
    rotate_array = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotate_array[j][n-i-1] = array[i][j]
    return rotate_array


def check(new_lock): # 키와 자물쇠가 딱 들어맞는지 체크
    len_lock = len(new_lock) // 3
    for i in range(len_lock):
        for j in range(len_lock):
            if new_lock[i+len_lock][j+len_lock] != 1:
                return False
    return True


def solution(key, lock):
    n, m = len(lock), len(key)
    new_lock = [[0 for _ in range(n*3)] for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for i in range(4):
        key = rotate_array_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j] # 키가 맞나 넣어보기

                if check(new_lock) == True: # 키가 맞는지 확인하기
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j] # 넣었던 키 다시 빼기

    return False
