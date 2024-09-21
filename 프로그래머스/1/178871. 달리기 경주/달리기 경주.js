// callings에서 부르는 순서대로 추월
// callings만큼 players를 다 순회할 순 없음
// 그런데 저장했다가 한번에 바꾸면 순서에 예외가 있을 수 있음 -> 바로바로 바꿔야함
// 객체에 저장
// 1. players를 key로 갖고 value는 등수인 객체 생성
// 2. callings에서 하나씩 꺼내 -1번째랑 value 변경

function solution(players, callings) {
    // { mumu: 1 ,  soe: 2 ,  poe: 3 ,  kai: 4 ,  mine: 5 }
    const mapper = {};
    
    players.forEach((player, idx) => {
        mapper[player] = idx
    });
    
    callings.forEach((calling, idx) => {
        curRank = mapper[calling]
        mapper[calling] -= 1
        mapper[players[curRank-1]] += 1
        let temp = players[curRank]
        players[curRank] = players[curRank-1]
        players[curRank-1] = temp
    })
    return players
}