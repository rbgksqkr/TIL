from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    if (sum1+sum2) % 2 != 0: 
        return -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    length = len(queue1)
    while answer <= length*3:
        if sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
            answer += 1
        elif sum1 > sum2:
            sum2 += queue1[0]
            sum1 -= queue1[0]
            queue2.append(queue1.popleft())
            answer += 1
        else: 
            break
    if sum1 != sum2:
        return -1
    return answer