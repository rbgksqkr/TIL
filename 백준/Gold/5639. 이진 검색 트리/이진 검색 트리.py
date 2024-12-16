import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 트리 저장
tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break


def post(start, end):
    # 루트 노드보다 큰 값이 나오면 오른쪽 서브트리 시작
    if start > end:
        return

    # 모든 요소가 루트 노드보다 작을 경우
    mid = end + 1

    for i in range(start + 1, end + 1):
        if tree[i] > tree[start]:
            mid = i
            break

    post(start + 1, mid - 1)  # 왼쪽 트리
    post(mid, end)  # 오른쪽 트리
    print(tree[start])


post(0, len(tree)-1)
