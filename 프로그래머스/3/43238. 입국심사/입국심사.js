// n명 줄서기. 심사관마다 심사 시간 다름.
// 한 심사대. 한 명만 심사.
// 더 빨리 끝나는 심사대가 있으면 그곳에서 심사.
// TODO: 모든 사람이 심사를 받는데 걸리는 시간의 최솟값

// 무조건 자리나면 가는게 아니라면, 다른 심사의 남은 시간도 알아야 한다.
// 심사시간 + 남은시간을 배열로 저장 -> 최솟값읆 못정함 -> 남은 시간을 배열로 저장하고 비교할 때 더하기?

// FIXME: 
// left에는 최소 시간, right에는 최대 시간.
// right : 최고 오래 걸리는 사람이 n명을 다 검사했을 때의 값
// times만큼 반복문을 도는데, 해당 심사관이 검사할 수 있는 사람수 = mid / times[i]
// 이 값이 n명을 넘으면 그 값과 answer 비교해서 최솟값 저장

function solution(n, times) {
    
    times.sort((a, b) => a - b);
    
    let left = 0;
    let right = n*times[times.length - 1];
    var answer = right;
    while (left <= right){
        let mid = Math.floor((left + right) / 2);
        let count = 0;
        for(let time of times){
            count += Math.floor(mid / time);
            
            if (count >= n){
                answer = Math.min(answer, mid);
            }
        }
        
        if(count >= n){
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return answer;
}