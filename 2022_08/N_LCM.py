import math
def solution(arr):
    while len(arr) > 1:
        a, b = arr.pop(), arr.pop()
        temp = math.gcd(a, b)
        arr.append(a*b // temp)
    return arr[0]
