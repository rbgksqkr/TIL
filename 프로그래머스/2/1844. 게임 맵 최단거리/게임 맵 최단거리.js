// nxm 2차원 배열. 1 이 빈칸, 0이 벽.
// TODO: 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값
// 상대 팀 진영에 도착할 수 없을 때는 -1

// 1. BFS로 구현한다.
// 2. 동서남북을 체크하여 visited 하지 않았고, 빈 칸(1)이면 push

let dx = [-1, 1, 0, 0];
let dy = [0, 0, -1, 1];

const getVisited = (row, col) =>
  Array(row)
    .fill(null)
    .map(() => Array(col).fill(false));

function solution(maps) {
    var answer = 0;
    
    let cur = [0 ,0];
    
    let queue = [[0, 0]]
    const n = maps.length;
    const m = maps[0].length;
    let visited = getVisited(n, m)
    
    visited[0][0] = 1;
    
    
    while (queue.length > 0){
        [x, y] = queue.shift();
        
        for (let i = 0; i < 4; i++){
            mx = x + dx[i]
            my = y + dy[i]
            
        
            if (mx < 0 || my < 0 || mx >= n || my >= m){
                continue;
            }
            
        
            if (!visited[mx][my] && maps[mx][my] == 1){
                visited[mx][my] = visited[x][y] + 1
                queue.push([mx, my])
            }
        }
    }
    
    
    return visited[n-1][m-1] == false ? -1 : visited[n-1][m-1];
}