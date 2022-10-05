import copy

n = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))  # 0:+, 1:-, 2:*, 3:/ 개수
result = []


def dfs(idx, answer, oper):
    if n == idx:
        result.append(answer)
        return
    for i in range(4):
        if oper[i] != 0:
            if i == 0:
                temp = copy.deepcopy(oper)
                temp[i] -= 1
                dfs(idx+1, answer+numbers[idx], temp)
            elif i == 1:
                temp = copy.deepcopy(oper)
                temp[i] -= 1
                dfs(idx+1, answer-numbers[idx], temp)
            elif i == 2:
                temp = copy.deepcopy(oper)
                temp[i] -= 1
                dfs(idx+1, answer*numbers[idx], temp)
            elif i == 3:
                temp = copy.deepcopy(oper)
                temp[i] -= 1
                if answer < 0:
                    answer = abs(answer)
                    answer = answer // numbers[idx]
                    answer = -answer
                    dfs(idx+1, answer, temp)
                else:
                    dfs(idx+1, answer//numbers[idx], temp)


answer = numbers[0]
dfs(1, answer, operations)
print(max(result))
print(min(result))
