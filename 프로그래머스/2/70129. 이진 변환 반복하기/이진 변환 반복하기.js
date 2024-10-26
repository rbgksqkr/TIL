// s가 '1'이 될 때까지 계속 s에 이진 변환
// 
// TODO: 이진 변환 횟수와 제거된 모든 0의 개수를 각각 배열에 담아 return
function solution(s) {
    var answer = [];
    let zeroCount = 0;
    let total = 0;
    
    while (s != '1'){
        let [zero, one]  = countBinary(s);
        zeroCount += zero;
        s = one.toString(2);   
        total += 1
    }
    
    return [total, zeroCount]

}

function countBinary(s) {
    let zeroCount = 0;
    let oneCount = 0;
    for(num of s){
        if(num === '0') zeroCount += 1;
        else oneCount += 1;
    }
    return [zeroCount, oneCount];
}
