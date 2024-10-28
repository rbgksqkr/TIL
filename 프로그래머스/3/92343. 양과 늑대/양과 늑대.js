// 1. edges를 이용해 연결 정보를 저장한다.
// 2. dfs탐색 진행, current, nextNodes, sheep, wolf를 인자로 넘겨준다.
// 3. 현재 점이 양인지 늑대인지 체크하고, 카운팅한다.
// 4. 늑대의 수가 양의 수보다 많다면, return하고
//    아니라면, 현재의 양의 수와 maxCount를 비교하고 갱신한다.
// 5. 갈 수 있는 노드들과 자식노드들을 합치고, 현재 노드를 제거한다.
// 6. 갈 수 있는 노드들로 dfs 탐색을 진행한다.

function solution(info, edges) {
    let answer = 0;
    let connectedNode = Array.from({ length: info.length }, () => []);
    
    for (let [from, to] of edges) {
      connectedNode[from].push(to);
    }
    
  function dfs(current, nextNodes, sheep, wolf) {
    info[current] === 0 ? sheep++ : wolf++;
    if (wolf >= sheep) return;
    if (answer < sheep) answer = sheep;

    let possibleNodes = [...nextNodes, ...connectedNode[current]];
    possibleNodes.splice(nextNodes.indexOf(current), 1);
    for (let next of possibleNodes) {
      dfs(next, possibleNodes, sheep, wolf);
    }
  }

  dfs(0, [0], 0, 0);
    
  return answer; 
}

