from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_cnt = 0
    trucks = deque(truck_weights)
    on_bridge = deque()
    while trucks:
        on_bridge.append(trucks.popleft())
        while trucks:
            if sum(on_bridge) + trucks[0] > weight:
                answer += bridge_length
                on_bridge.popleft()
                break
            else:
                on_bridge.append(trucks.popleft())
                answer += 1
                print(on_bridge)
        
    return answer
