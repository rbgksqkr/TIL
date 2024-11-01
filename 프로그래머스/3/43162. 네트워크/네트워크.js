function solution(n, computers) {
    var answer = 0;
    
    const visited = [];
    
    for (let i = 0; i < computers.length; i++){
        if(!visited[i]){ // 방문하지 않은 노드일 때
            dfs(i, computers, visited); // dfs
            answer += 1
        }
    }
    return answer;
}

function dfs(node, computers, visited){
    visited[node] = true;
    
    for(let i = 0; i < computers.length; i++){
        if(!visited[i] && computers[node][i] == 1){
            dfs(i, computers, visited)
        }
    }
}