function solution(n) {
    var answer = 1;
    
    const start = Math.ceil(n / 2);
    
    for (let i = n; i > 0; i--){
        let count = i;
        for (let j = i - 1; j > 0; j--){
            count += j;
            
            if (count == n) {
                answer += 1;
            }
            
            if (count >= n) break;
            
        }
    }
    return answer;
}