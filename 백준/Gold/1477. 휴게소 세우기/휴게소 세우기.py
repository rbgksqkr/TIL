import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [l]
arr.sort()

start, end = 1, l-1
answer = 0
while start <= end:
    count = 0
    mid = (start+end) // 2
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > mid: # 기존의 최댓값보다 작게 휴게소를 다 세우고 M개가 지어졌는 지 확인
            count += (arr[i]-arr[i-1]-1) // mid
    if count > m: # 더 많이 세워야하면 휴게소 사이 거리를 늘린다 (start = mid+1)
        start = mid+1
    else: # 더 적게 세워지면 휴게소 사이 거리를 좁힌다 (end = mid-1, count == m: answer = mid)
        end = mid-1
        answer = mid

print(answer)
