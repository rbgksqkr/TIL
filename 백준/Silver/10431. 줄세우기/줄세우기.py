# 항상 20명
# 같은 키를 가진 학생은 한 명도 없어
# 키 순서대로 번호를 부여. 키가 가장 작은 아이가 1번, 그 다음이 2번.
# 아무나 한 명을 뽑아 줄의 맨 앞에 세운다.
# 학생이 한 명씩 줄의 맨 뒤에 서면서 다음 과정을 거친다.
# 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
# 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다.
# 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.

# 아이들의 키가 주어지고, 어떤 순서로 아이들이 줄서기를 할 지 주어진다.
# 줄서기가 끝났을 때 학생들이 총 몇 번 뒤로 물러서게 될까?
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    students = list(map(int, input().split()))
    num = students[0]
    answer = 0
    for i in range(1, len(students)-1):
        for j in range(i+1, len(students)):
            if students[i] > students[j]:
                students[i], students[j] = students[j], students[i]
                answer += 1
    print(num, answer)
