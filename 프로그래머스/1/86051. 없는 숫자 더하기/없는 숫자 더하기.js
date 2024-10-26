// 0~9 정수 배열 numbers
// 0~9 숫자 중 numbers 안에 없는 숫자의 합

function solution(numbers) {
    var answer = 0;
    
    for(let i =0; i <= 9; i++){
        if(!numbers.includes(i)){
            answer += i
        }
    }
    
    return answer;
}