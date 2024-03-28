import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()


def binary_search(start, end, target, arr):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


answer = []
for idx, i in enumerate(a):
    temp = binary_search(0, m-1, i, b)
    if temp == -1:
        answer.append(a[idx])
print(len(answer))
for i in answer:
    print(i, end=' ')
