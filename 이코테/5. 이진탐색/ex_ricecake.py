n, m = map(int, input().split())

cakes = list(map(int, input().split()))
cakes.sort()

def binary_search(array, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total_len = sum([i-mid for i in array if i-mid > 0])
        
        if total_len >= m:
            result = mid
            start = mid + 1
        
        else:
            end = mid - 1

    return result

print(binary_search(cakes, 0, cakes[-1]))
    

# 4 6
# 19 15 10 17