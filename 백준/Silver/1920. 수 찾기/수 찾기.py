import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            print(1)
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    print(0)
    return None


for target in b:
    binary_search(a, target, 0, n-1)
