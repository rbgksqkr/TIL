// 중앙은 노란색. 테두리는 갈색.
// 갈색 격자 개수. 노란 격자 개수.
// (x-2)(y-2) = yellow
// x*y = brown + yellow
// (brown + yellow) / x = y

function solution(brown, yellow) {
    var answer = [];
    let total = brown + yellow;
    
    for (let x = 3; x <= total/x; x++){
        y = Math.floor(total / x);
        
        if ((x-2)*(y-2) == yellow){
            if(x < y){
                [x, y] = [y, x]
            }
            
            return [x, y];
        }
    }
    
}