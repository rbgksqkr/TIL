// 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만든다.
// TODO: 타겟 넘버를 만드는 방법 개수

// 1. 각 숫자들의 +, - 를 만든다.
// 2. 

function solution(numbers, target) {
    const answer = [];
    
    const data = [];
    
    for(let number of numbers){
        data.push([number, -number]);
    }
    
    return bfs(data, numbers.length, target);
}

function bfs(data, length, target){
    let queue = [...data.shift()];
    let count = 0;
    
    for (let [minus, plus] of data){
        
        const temp = [];
        while (queue.length > 0){
            
            const data = queue.pop();
            
            temp.push(data + minus);
            temp.push(data + plus);
        }
        queue = [...temp]
    }
    
    for (let number of queue){
        if(number == target) {
            count += 1;
        }
    }
    
    return count;
      
}