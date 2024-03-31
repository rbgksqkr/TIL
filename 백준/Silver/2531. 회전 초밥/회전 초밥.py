# k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
# 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공
# 만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공
# 초밥 종류 최댓값 구하기

# --- 구현 방법 ---
# 없을 경우 요리사가 새로 만들어 제공 -> 무조건 포함 X
# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
# start가 N이 될 때까지 세기
# k개 이하로 먹을 수도 있음
# k <= N 이므로 한바퀴 이상 돌지 않음
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

plates = []
for _ in range(n):
    plates.append(int(input()))

start = 0
end = 1

# start 부터 k개를 슬라이싱 후 set으로 묶어서 중복 확인. plates[start:start+k]
# set의 길이 체크 후 max length 계산

max_count = 0
while start < n:
    temp = set()
    if start + k > n:
        temp = set(plates[start:] + plates[:(start+k) % n])
    else:
        temp = set(plates[start:start+k])
    temp.add(c)
    max_count = max(max_count, len(temp))
    start += 1
    end += 1

print(max_count)
