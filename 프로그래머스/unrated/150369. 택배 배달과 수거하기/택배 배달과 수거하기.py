def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_value, pickup_value = 0, 0
    for i in range(n-1, -1, -1):
        delivery_value += deliveries[i]
        pickup_value += pickups[i]
        
        while delivery_value > 0 or pickup_value > 0:
            delivery_value -= cap
            pickup_value -= cap
            answer += (i+1) * 2
    
    return answer