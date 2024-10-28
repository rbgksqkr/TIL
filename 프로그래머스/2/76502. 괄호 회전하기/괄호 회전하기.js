// 1. 문자열을 하나씩 스택에 넣는다.
// 2. 하나씩 꺼내서 비교한다.
function solution(s) {
    var answer = 0;
    const stack = [];
    let flag = 1;
    
    let temp = s;
    
    for (let i = 0; i < s.length; i++){
        temp = temp.slice(i) + temp.slice(0, i)
        for (let str of temp){
            console.log(temp);
        }
    }
    
    return answer;
}