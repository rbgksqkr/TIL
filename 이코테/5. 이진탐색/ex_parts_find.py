n = int(input())
parts = list(map(int, input().split()))
m = int(input())
orders = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return "yes"
        
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "no"

parts.sort()
for order in orders:
    print(binary_search(parts, order, 0, len(parts)-1), end=' ')

# 5
# 8 3 7 9 2
# 3
# 5 7 9