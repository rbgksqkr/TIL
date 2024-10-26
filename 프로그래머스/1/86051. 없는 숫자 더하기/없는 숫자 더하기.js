// 0~9 정수 배열 numbers
// 0~9 숫자 중 numbers 안에 없는 숫자의 합

function solution(numbers) {
    var answer = 0;
    const data = Array.from({length: 10}, (_, i) => i);
    
    for(i of data){
        if(!numbers.includes(i)){
            answer += i
        }
    }
    
    return answer;
}