function solution(n, computers) {
    let visited = [false];
    let answer = 0;

    function dfs(i) {
        visited[i] = true; // 자기 자신 방문 처리
        for(let j=0; j<computers[i].length; j++) {
            if(computers[i][j]===1 && !visited[j]){ // i 에서 j 로 갈 수 있고 && 방문하지 않았음
                dfs(j);
            }
        }
    }
    
    for (let i=0; i < computers.length; i++) {
        if (!visited[i]) { // 방문하지 않았음
            dfs(i) // dfs 돌려
            answer++; // 이어진만큼만 방문 체크
        }
    }
    
    return answer;
}