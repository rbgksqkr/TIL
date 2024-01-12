import sys
input = sys.stdin.readline

n = int(input())

board = []
count = 0

isUsed1 = [0 for _ in range(40)]
isUsed2 = [0 for _ in range(40)]
isUsed3 = [0 for _ in range(40)]


def func(cur):
    global count
    if cur == n:
        count += 1
        return

    for i in range(n):
        if isUsed1[i] or isUsed2[cur+i] or isUsed3[cur-i+n-1]:
            continue
        isUsed1[i] = 1
        isUsed2[cur+i] = 1
        isUsed3[cur-i+n-1] = 1
        func(cur+1)
        isUsed1[i] = 0
        isUsed2[cur+i] = 0
        isUsed3[cur-i+n-1] = 0


func(0)
print(count)
