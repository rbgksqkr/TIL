import sys
input = sys.stdin.readline


n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0


def func(cur, total):
    global count
    if cur == n:
        if total == s:
            count += 1
        return

    func(cur+1, total)
    func(cur+1, total + arr[cur])


func(0, 0)
if s == 0:
    count -= 1
print(count)