def solve(N, M, trees):
    # 이진 탐색을 위한 시작점과 끝점
    start, end = 0, max(trees)

    result = 0
    while start <= end:
        mid = (start + end) // 2

        # 잘려서 가져갈 수 있는 나무의 길이를 계산
        total = 0
        for tree in trees:
            if tree > mid:
                total += tree - mid

        # 충분한 나무(M 이상)를 얻을 수 있으면
        # 절단기의 높이를 더 높일 수 있는지 확인해야 함.
        if total >= M:
            result = mid  # 일단 현재 mid 값은 유효하므로 기록
            start = mid + 1
        else:
            # 나무가 부족하므로 더 낮게 잘라야 함
            end = mid - 1

    return result

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    # 예시 입력
    # 첫째 줄: 나무의 수 N, 필요한 나무 길이 M
    # 둘째 줄: 나무의 높이 리스트
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    
    answer = solve(N, M, trees)
    print(answer)
