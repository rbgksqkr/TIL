# 2차원 배열에서 이분 탐색
# 어떻게 생각함 이걸????
# 1. N이 10만이라 N^2 순회도 안되고, NxN은 정렬도 못시킨다.
# 2. 만들어진 일차원 배열 B를 정렬할 생각을 하지 말고, 이미 정렬된 일차원 배열에서 해당 인덱스를 찾아야 한다.
# 3. A[i][j] = i*j 이므로, 찾는 값을 행으로 나눈 결과값(mid//i)이 찾는 값보다 작거나 같은 수의 개수가 된다.
# 4. 찾는 값이 N*N 배열이므로 N을 초과할 수 없기 때문에, N보다 크면 N으로 계산한다(min(mid//i, N)
# 5. 해당 숫자(mid)보다 작거나 같은 숫자들을 전부 찾아줌으로써 mid가 몇번째에 위치한 숫자인지 알아낼 수 있다.

N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N) #mid 이하의 i의 배수 or 최대 N
    
    if temp >= K: #이분탐색 실행
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)