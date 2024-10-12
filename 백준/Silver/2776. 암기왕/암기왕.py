import sys
input = sys.stdin.readline

T = int(input())


def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True

        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


for _ in range(T):
    n = int(input())
    note1 = list(map(int, input().split()))

    m = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()
    for i in range(m):
        target = note2[i]

        start, end = 0, n-1
        if binary_search(note1, start, end):
            print(1)
        else:
            print(0)
