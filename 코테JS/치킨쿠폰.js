function solution(chicken) {
    let answer = 0;
    let coupon = chicken;
    const ORDER_CHICKEN = 10;
    while (coupon >= 10){
        answer += parseInt(coupon / ORDER_CHICKEN);
        coupon = parseInt(coupon / ORDER_CHICKEN) + coupon % ORDER_CHICKEN;
    }
    return parseInt(answer);
}
