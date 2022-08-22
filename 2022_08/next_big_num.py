def solution(n):
    ones = bin(n).count('1')
    while True:
        n += 1
        temp = bin(n).count('1')
        if temp == ones:
            return n
