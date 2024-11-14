# 제거할 n개의 바위를 결정해야 한다.
# 바위를 제거 후 각 바위 사이의 거리를 계산한다.
# 1, 2개도 아니고 n개를 어떻게 시간복잡도를 고려해서 제거하지?

# 1. 바위를 정렬하고, 마지막 rock과 도착 바위와의 거리를 계산하기 위해 추가한다.

# 2. parametric search -> 거리를 이분탐색으로 결정하여, 해당 거리일 때 몇개를 놓을 수 있는지 체크한다.
# 3. 거리의 최솟값과 최댓값을 1, distance로 잡는다
# 4. n개 이상 놓을 경우 -> 값 저장 후 end = mid - 1, 미만 일 경우 -> start = mid + 1

def solution(distance, rocks, n):
    
    # 1. 바위를 정렬하고, 마지막 rock과 도착 바위와의 거리를 계산하기 위해 추가한다.
    rocks.sort()
    rocks.append(distance)
    
    # 3. 거리의 최솟값과 최댓값을 1, distance로 잡는다.
    start, end = 1, distance
    
    answer = -1
    while start <= end:
        mid = (start + end) // 2
        
        delete = 0 # 제거한 바위 개수
        prev_rock = 0 # 이전 바위의 위치
        
        for rock in rocks:
            dist = rock - prev_rock
            # 거리가 커트라인 보다 작다면, 바위를 제거
            if dist < mid:
                delete += 1
                if delete > n:
                    break
            # 바위를 제거하지 않았다면, prev_rock을 갱신
            else:
                prev_rock = rock
        
        if delete > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    
    return answer