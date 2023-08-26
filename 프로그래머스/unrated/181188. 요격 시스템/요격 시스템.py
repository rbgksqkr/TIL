def solution(targets):
    targets.sort(key=lambda x:x[1])
    shoot = -1
    count = 0
    for target in targets:
        if shoot < target[0]:
            count += 1
            shoot = target[1] - 0.5
    return count
