// 금액 지불. 10일동안 회원 자격.
// 매일 한 가지 제품 할인.
// 하루에 하나씩만 구매
// 제품과 수량이 할인하는 날짜와 10일 연속으로 일치하는 경우에 맞춰 회원가입
// TODO: 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를

// want: number 하고, 날짜 인덱스만큼 체크했을 때 다 있으면 += 1

function solution(want, number, discount) {
    var answer = 0;
    
    let data = {};
    for (let i = 0; i < want.length; i++){
        data[want[i]] = number[i]
    }
    
    
    
    
    
    for (let i = 0; i < discount.length-9; i++){
        let count = JSON.parse(JSON.stringify(data));
        for(let fruit of discount.slice(i, i+10)){
            if(count[fruit]){
                count[fruit] -= 1;    
            }
        } 
        
        const values = Object.values(count);
        if (values.every((count) => count === 0)){
            answer += 1;
        }
    }

    
    return answer;
}