// 숫자 문자열 t, p. t에서 p와 길이가 같은 부분 문자열 중 p보다 작거나 같은 것이 나오는 횟수
// 1. t에서 p의 길이인 부분 문자열 뽑기
// 2. 1에서 뽑은 부분 문자열 중 p보다 작거나 같은 수의 개수

function solution(t, p) {
    var answer = 0;
    const target = Number(p);
    const length = p.length;
    
    for(let i = 0; i <= t.length-length; i++){
        const number = Number(t.slice(i, i+length))
        if (number <= target){
            answer += 1;
        }
    }
    return answer;
}