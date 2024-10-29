// N명이 참가하고, 토너먼트 형식으로 진행
// 1 ~ N 차례로 배정.
// 1 <-> 2, 3 <-> 4 ... 게임 진행
// 이긴 사람이 다음 라운드 진출
// 다음 라운드 진출 참가자 번호 : 1번 - N/2번
// A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다

// TODO: A가 B를 몇 라운드에서 만나는가?
// 1. 다음 라운드 번호 : Math.ceil(k / 2)
// 2. answer += 1 하고, 다음 번호 할당

function solution(n,a,b)
{
    var answer = 0;
    
    while(Math.abs(a - b)) {
        a = Math.ceil(a / 2)    
        b = Math.ceil(b / 2)
        answer += 1
    }
    

    

    return answer;
}