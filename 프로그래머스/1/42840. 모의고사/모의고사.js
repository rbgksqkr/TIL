// 1, 2, 3, 4, 5
// 2, 1, 2, 3, 2, 4, 2, 5
// 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
// 배열 곱하기 안되네. 배열 반복 어캐함?
// 최댓값을 가진 배열 요소
function solution(answers) {
    // var answer = [];
    let first = [1, 2, 3, 4, 5];
    let second = [2, 1, 2, 3, 2, 4, 2, 5];
    let third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    
    
    const count = {1: 0, 2: 0, 3: 0};
    console.log(count);

    for(let i = 0; i < answers.length; i++){
        if(first[i % 5] == answers[i]){
            count['1'] += 1
        } if (second[i % 8] == answers[i]){
            count['2'] += 1;
        } if (third[i % 10] == answers[i]) {
            count['3'] += 1
        }
    }
    
    const result = Object.values(count);
    const maxValue = Math.max(...result);
    const items = Object.entries(count);
    
    const answer = [];
    for(let [key, value] of items){
        if(value == maxValue){
            answer.push(Number(key));
        }
    }

    answer.sort();
    return answer;
}