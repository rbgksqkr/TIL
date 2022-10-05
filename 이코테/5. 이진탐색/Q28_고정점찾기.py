def binary_search(array, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    
    else:
        return binary_search(array, mid + 1, end)

n = int(input())
numbers = list(map(int, input().split()))


answer = binary_search(numbers, 0, n-1)

if answer == None:
    print(-1)
else:
    print(answer)

    