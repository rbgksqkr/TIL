import sys
input = sys.stdin.readline

n = int(input())  # 센서
k = int(input())  # 집중국
sensors = list(map(int, input().split()))
sensors.sort()

if n <= k:
    print(0)
else:
    distances = []
    for i in range(1, n):
        distances.append(sensors[i] - sensors[i-1])
        
    distances.sort()
    for i in range(k-1):
        distances.pop()
    print(sum(distances))
