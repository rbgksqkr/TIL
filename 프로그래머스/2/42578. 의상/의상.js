// TODO: 서로 다른 옷의 조합의 수

// 각 종류별로 최대 1가지 의상만 가능
// 1개만 입는 것도 되고, 추가로 입는 것도 다른 종류에 포함
// 아무것도 안입는 경우는 없음

// 1. 종류별로 분류
// 2. 종류별로 1가지 의상만 가능하니까 안입는 경우 포함하여 +1 해서 곱하기
// 3. 아무것도 안입는 경우를 제외하기 위해 -1

function solution(clothes) {
    var answer = 1;
    // 1. 종류별로 분류
    let obj = clothes.reduce((acc, cur) => {
        acc[cur[1]] ? acc[cur[1]] += 1 : acc[cur[1]] = 1
        return acc;
    }, {})
    
    let values = Object.values(obj);
    
    // 2. 종류별로 1가지 의상만 가능하니까 안입는 경우 포함하여 +1 해서 곱하기
    for(value of values) {
        answer *= value + 1
    }
    
    // 3. 아무것도 안입는 경우를 제외하기 위해 -1
    return answer - 1;
}