// 1. 문자열을 하나씩 스택에 넣는다.
// 2. 하나씩 꺼내서 비교한다.
function solution(s) {
    var answer = 0;
    
    if (s.length % 2 == 1) return 0;
    
    for (let i = 0; i < s.length; i++){
        const stack = [];
        let flag = 1;
        let temp = s.slice(i) + s.slice(0, i)
        
        for (let str of temp){
            if (str == '(' || str == '{' || str == '['){
                stack.push(str);
            } else {
                const bracket = stack.pop();
                
                // 현재 소괄호가 닫혀야되는데, 가장 최근 요소가 여는 소괄호면 계속 순회
                if (str == ')' && bracket == '(') continue;
                if (str == '}' && bracket == '{') continue;
                if (str == ']' && bracket == '[') continue;
                
                flag = 0;
                break;
            }
        }
        
        if(flag) answer += 1;
    }
    
    return answer;
}