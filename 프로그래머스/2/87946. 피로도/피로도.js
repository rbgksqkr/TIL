// [최소 필요 피로도, 소모 피로도]
// TODO: 유저가 탐험할 수 있는 최대 던전 수(answer)
// 1 <= k <= 5000. 던전 수 <= 8. 완전탐색 가능.



function solution(k, dungeons) {
    let n = dungeons.length;
    let m = dungeons[0].length;
    
    let data = [];
    let visited = Array(dungeons.length).fill(false);
    const curDungeons = pickDungeons(data, dungeons, visited, k);
    
    
    return result;
}

var result = 0;

function solve(data, k){
    let answer = 0;
    for (let dungeon of data){
        [required, minus] = dungeon;
        if(k >= required){
            k -= minus;
            answer += 1;
        }
    }
    
    result = Math.max(result, answer);
}

function pickDungeons(data, dungeons, visited, k){
    if (data.length == dungeons.length){
        solve(data , k);
        return;
    }
    
    for (let i = 0; i < dungeons.length; i++){
        if(!visited[i]){
            visited[i] = true;
            data.push(dungeons[i]);
            pickDungeons(data, dungeons, visited, k);
            visited[i] = false;       
            data.pop();
        }
    }
    
}

