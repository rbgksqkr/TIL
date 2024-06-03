# --- 요구 사항 ---
# 팀원 수에는 제한이 없다. 한 팀만 있을 수도 있다.
# 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다.
# 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다. (단, 단 한 명만 선택할 수 있다.)
# TODO: 주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산

# --- 문제 풀이 ---
# 주어진 선택의 결과를 통해 사이클을 이룰 수 있으면 한 팀
# 자기 자신을 택한 경우 사이클은 이룰 수 없지만 자기 자신은 하나의 팀으로 인정
# 하나의 트리에 있으면 하나의 팀
# 첫과 끝이 이어진 순환 사이클이 되어야한다.

import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline


def dfs(x):
    global team_count

    target = choices[x]  # 가리킨 사람
    teams.append(x)  # 나를 팀 후보에 추가
    visited[x] = 1  # 내가 팀 후보에 포함

    if visited[target]:  # 가리킨 사람이 이미 선택된 경우
        if target in teams:
            team_count += len(teams[teams.index(target):]) # 사이클이 형성된 이후의 팀 후보의 인원들이 모두 팀

    else:  # 가리킨 사람이 선택되지 않았던 사람인 경우
        dfs(target)


T = int(input())

for _ in range(T):

    n = int(input())
    choices = [0] + list(map(int, input().split()))

    visited = [0 for _ in range(n+1)]
    team_count = 0

    for i in range(1, n+1):
        if not visited[i]:
            teams = []
            dfs(i)
    print(n-team_count)
