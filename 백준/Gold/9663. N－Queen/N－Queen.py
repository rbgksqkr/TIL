import sys
input = sys.stdin.readline

n = int(input())

answer = 0
row = [0 for _ in range(n)]  # 1행에 1개밖에 못놓으므로 row 1차원 배열로 선언.
board = [[0 for _ in range(n)] for _ in range(n)]


def check(x):
    for i in range(x):
        # 같은 열인지 확인.
        # 대각선 체크.
        # 맨 윗 행부터 채우므로 x보다 작은 값만 체크.
        # x와 i의 세로길이와 가로길이가 같으면 대각선에 위치한 것으로 체크.
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def queen(x):
    global answer
    if x == n:  # 탈출 조건. 퀸 n개를 보드판에 모두 배치.
        answer += 1
        return

    # (x, i)에 퀸을 놓겠다
    for i in range(n):
        row[x] = i  # 일단 배치하고
        if check(x):  # promising 한 위치에
            queen(x+1)  # 다음 퀸 배치


queen(0)
print(answer)