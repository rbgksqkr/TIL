from collections import deque
import sys
input = sys.stdin.readline
T = int(input())


def calculationD(n):
    return (2*n) % 10000


def calculationS(n):
    if n == 0:
        return 9999
    else:
        return n-1


def calculationL(n):
    front = n % 1000
    back = n // 1000
    res = front*10 + back
    return res


def calculationR(n):
    front = n % 10
    back = n // 10
    res = front*1000 + back
    return res


for _ in range(T):
    now_num, target_num = map(int, input().split())
    visited = set()
    queue = deque()
    queue.append((now_num, ''))
    visited.add(now_num)
    while queue:
        num, result = queue.popleft()
        if num == target_num:
            print(result)
            break
        
        temp = calculationD(num)
        if temp not in visited:
            visited.add(temp)
            queue.append((temp, result+'D'))
        temp = calculationS(num)
        if temp not in visited:
            visited.add(temp)
            queue.append((temp, result+'S'))
        temp = calculationL(num)
        if temp not in visited:
            visited.add(temp)
            queue.append((temp, result+'L'))
        temp = calculationR(num)
        if temp not in visited:
            visited.add(temp)
            queue.append((temp, result+'R'))
