from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_weight = 0
    bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    
    while len(bridge) != 0:
        left = bridge.popleft()
        bridge_weight -= left
        time += 1
        if trucks:
            if bridge_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge_weight += truck
                bridge.append(truck)
            else:
                bridge.append(0)
                  
    return time
