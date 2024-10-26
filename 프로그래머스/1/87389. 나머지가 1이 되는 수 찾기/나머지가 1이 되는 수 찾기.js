function solution(n) {
    for (let i = 1; i < n; i++){
        const rest = n % i
        if (rest == 1) return i
    }
}