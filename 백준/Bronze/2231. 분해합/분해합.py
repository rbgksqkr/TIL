import sys
input = sys.stdin.readline

n = int(input())

flag = 0
for i in range(n):
    str_list = list(map(int, list(str(i))))

    temp = i + sum(str_list)

    if temp == n:
        print(i)
        flag = 1
        break

if flag == 0:
    print(0)
