// 종류별 1가지만 착용
// 의상 종류별로 분리
// 1개씩 착용 + 가짓수 곱하기 -> 모든 옷을 다 입을 필요 없음 -> 해당 옷을 안입는 경우도 포함

function solution(clothes) {
    var answer = 1;
    const kind = {};
    
    clothes.forEach((cloth) => {
        if(kind[cloth[1]]){
            kind[cloth[1]] += 1
        } else {
            kind[cloth[1]] = 1
        }
    });
        
    for(const key in kind) {
        answer *= (kind[key] + 1);		
    }
    return answer - 1;
}