// max값 구하기. max값 여러개여도 한가지만 반환.

function solution(nums) {
    var answer = 0;
    const result = [...new Set(nums)];
    
    return result.length < Math.floor(nums.length / 2) ? result.length : Math.floor(nums.length / 2);
    
}