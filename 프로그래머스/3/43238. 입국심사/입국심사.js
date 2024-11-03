// n명 입국심사 대기.
// 더 빨리 끝나는 심사대가 있으면 기다렸다가 심사.
// TODO: 모든 사람이 심사를 받는데 걸리는 시간의 최솟값

//  n이 10억. O(logn) 필요 -> 이분탐색
// 시간을 정하기 어려움 -> 결정 문제
// 모든 사람이 심사를 받는데 걸리는 시간의 최솟값 -> x분이면 n명이 심사를 받을 수 있는가?

function solution(n, times) {
    times.sort((a, b) => a - b);
    
    let start = 0;
    let end = n*times[times.length - 1];
    let answer = end;
    
    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        let count = 0;
        
        for (let i = 0; i < times.length; i++){
            count += Math.floor(mid / times[i]);
            
            if (count >= n){
                answer = Math.min(answer, mid);
            }
        }
        
        if (count >= n){
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    
    return answer;
}