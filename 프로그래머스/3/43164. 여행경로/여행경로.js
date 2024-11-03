// 항상 ICN 에서 출발. 항공권을 모두 이용하여 여행 경로 짜기.
// 공항 수는 3개 이상 10000개 이하. O(N^2) 이하.
// TODO: 방문하는 공항 '경로'를 배열로 반환

// 경로를 어떻게 저장하지? queue에 넣을 때마다 배열을 넣어?


// 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로
// 1. 인접 그래프 형식으로, 해당 공항에서 출발했을 때 갈 수 있는 공항을 배열로 저장
// 2. dfs로 모든 공항 돌기
// 3. dfs("ICN")
// 4. visited["ICN"] = 1; queue.push("JFK");
// {"ICN": ["JFK"], "HND": ["IAD"], "JFK": ["HAD"]}

// 결정 : visited["ICN"]["JFK"] = [...data, "JFK"]. 경로 저장.

const getVisited = (row, col) => Array(row).fill(null).map(() => Array(col).fill(null));

function solution(tickets) {
//     let set = new Set();
//     tickets.forEach((ticket) => {
//         set.add(ticket[0]);
//         set.add(ticket[1]);
//         });
//     const totalCount = set.size;
    
//     var answer = [];
//     const n = tickets.length;
//     const m = tickets[0].length;
    
//     let visited = getVisited(totalCount, totalCount);
//     console.log(visited)
    
//     tickets.forEach((ticket) => {
//         visited[ticket[0]]
//     })
    
    // 알파벳 순서가 앞서는 경로를 return
    // 출발역을 기준으로 오름차순 정렬
    // 출발역이 같다면 도착역 기준으로 오름차순 정렬
    tickets.sort();
    
    let answer = [];
    let result = []; // 방문 경로 저장
    const visited = [];
  
    const len = tickets.length;
    
    function dfs(str, count){ // 현재 출발역, 방문 공항 개수
        result.push(str);
        
        if (count == len){
            answer = result;
            return true;
        }
        
        for(let i = 0; i < len; i++){
            if(!visited[i] && tickets[i][0] == str){
                visited[i] = true;
                if(dfs(tickets[i][1], count + 1)) return true;
                visited[i] = false;
            }
        }
        
        result.pop()
        
        return false;
    }
    
    dfs("ICN", 0)
    
    return answer;
}