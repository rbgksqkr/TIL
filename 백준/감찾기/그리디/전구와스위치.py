import sys
import copy
input = sys.stdin.readline

n = int(input())
now = list(map(int, input().strip()))
target = list(map(int, input().strip()))

arr = []
copy_now = copy.deepcopy(now)
for i in range(2):
    copy_now[i] = abs(now[i]-1)
arr.append(now)
arr.append(copy_now)


def flip(x):
    if x == 0:
        return 1
    else:
        return 0


INF = int(1e9)
result = INF
for i in range(2):
    new_arr = arr[i]
    count = i
    for j in range(1, n):
        if new_arr[j-1] != target[j-1]:
            if j == n-1:
                new_arr[j-1] = flip(new_arr[j-1])
                new_arr[j] = flip(new_arr[j])
            else:
                new_arr[j-1] = flip(new_arr[j-1])
                new_arr[j] = flip(new_arr[j])
                new_arr[j+1] = flip(new_arr[j+1])
            count += 1

    if new_arr == target:
        result = min(result, count)
if result == INF:
    print(-1)
else:
    print(result)
