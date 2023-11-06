def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    
    parent = [i for i in range(n)]
    
    for data in costs:
        a, b, cost = data
        if find(a, parent) != find(b, parent):
            union(a, b, parent)
            answer += cost
    return answer