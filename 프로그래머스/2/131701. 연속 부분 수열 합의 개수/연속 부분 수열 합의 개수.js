// 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수의 종류
// 원형 수열: 일반적인 수열에서 처음과 끝이 연결된 형태의 수열
// 길이가 1인 연속 부분 수열 ... 길이가 n인 연속 부분 수열
// 1. elements를 2개 붙인다.
// 2. 길이가 1인 것부터 elements.length 까지 순회하며 answer에 추가
// 3. 다 돌면 Set으로 중복 제거

function solution(elements) {
    var answer = [];
    
    const data = [...elements, ...elements];
    console.log(data);
    
    for (let i = 1; i <= elements.length; i++){
        for (let j = 0; j < elements.length; j++){
            let temp = data.slice(j, j+i);
            answer.push(temp.reduce((acc, cur) => acc + cur, 0));
        }
    }
    
    return [...new Set(answer)].length;
}