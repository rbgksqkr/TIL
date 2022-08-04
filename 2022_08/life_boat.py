from collections import deque
def solution(people, limit):
    people.sort()
    people = deque(people)   
    answer = 0
    while people:
        weight = 0
        weight = people.pop()
        answer += 1
        if not people:
            break
        elif weight + people[0] <= limit:
            people.popleft()
    return answer
