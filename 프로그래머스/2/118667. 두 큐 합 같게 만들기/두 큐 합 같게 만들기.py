from collections import deque

def solution(queue1, queue2):
    n = len(queue1)
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    if (sum1 + sum2) % 2 != 0:
        return -1
    target = abs(sum1 + sum2) // 2
    
    start = 0
    end = n - 1
    queue3 = queue1 + queue2
    while sum1 != target:
        if sum1 < target:
            end += 1
            if end == 2*n:
                return -1
            sum1 += queue3[end]

        elif sum1 > target:
            sum1 -= queue3[start]
            start += 1
        answer += 1

    return answer