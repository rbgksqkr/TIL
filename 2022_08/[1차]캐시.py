from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    for city in cities:
        city = city.upper()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
            continue
        if cacheSize == 0:
            answer += 5
            continue
        if len(cache) == cacheSize and cacheSize > 0:
            cache.popleft()
        cache.append(city)
        answer += 5
    return answer
