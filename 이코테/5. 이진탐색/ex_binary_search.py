array = [0, 2, 3, 4, 6, 9, 10]

target = 10

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid       
        if array[mid] > target:
            end = mid - 1  
        else:
            start = mid + 1
    return None    

result = binary_search(array, target, 0, len(array)-1)
if result == None:   
    print("원소가 존재하지 않습니다.")
else:
    print(result)

