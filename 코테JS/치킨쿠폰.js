function solution(chicken) {
    let answer = 0;
    let coupon = chicken;
    const ORDER_CHICKEN = 10;
    while (coupon > 1){
        coupon = chicken / ORDER_CHICKEN;
        answer += coupon
        chicken = coupon        
    }

    return parseInt(answer);
}
