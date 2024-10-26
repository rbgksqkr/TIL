// 1. 특정 수의 약수의 개수 구하기
// 2. 약수의 개수가 홀수인지 짝수인지 판단하기
// 3. 약수의 개수가 짝수면 더하고, 홀수면 빼기
// 4. 1-3 과정을 left<=x<=right 사이를 순회하기

function solution(left, right) {
    var answer = 0;
    
    for (let k = left; k <= right; k++){
        // 1
        let count = 0;
        for (let i = 1; i <= k; i++){
            if (k % i == 0) {
                count += 1
            }
        }

        // 2, 3
        if (count % 2 == 0) {
            answer += k
        } else {
            answer -= k
        }
    
    }
    return answer;
}