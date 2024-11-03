// [최소 필요 피로도, 소모 피로도]
// 수가 작음. 완전 탐색 가능.
// TODO: 유저가 탐험할수 있는 최대 던전 수

// 1. 내가 탐헐할 던전 순서를 정한다.
// 2. 그 순서대로 돌았을 때 돌 수 있는 던전 수를 구한다.
// 3. 던전 수가 최대가 되도록 max값을 구한다.

function solution(k, dungeons) {
    var answer = -1;
    
    let visited = Array(dungeons.lenth).fill(0);
    
    function dfs(k, count){ // dfs(현재 피로도, 현재까지 돈 던전 수)
        answer = Math.max(answer, count);
        
        for(let i = 0; i < dungeons.length; i++){
            if(!visited[i] && k >= dungeons[i][0]){
                visited[i] = 1;
                dfs(k - dungeons[i][1], count + 1);
                visited[i] = 0;
            }
        }
    }
    
    dfs(k, 0);
    
    return answer;
}