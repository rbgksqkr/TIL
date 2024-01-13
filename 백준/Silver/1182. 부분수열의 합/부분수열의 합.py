import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0


def func(cur, total):
    global count
    if cur == N:
        if total == S:
            count += 1
        return
    func(cur+1, total)
    func(cur+1, total+arr[cur])
    # for i in range(N):
    #     if isUsed[i]:
    #         continue
    #     print('i, cur, count:', i, cur, count)

    #     isUsed[i] = 1
    #     print('arr[i]:', cur+arr[i])
    #     func(cur+arr[i])
    #     isUsed[i] = 0
func(0, 0)
if S == 0:
    count -= 1
print(count)
