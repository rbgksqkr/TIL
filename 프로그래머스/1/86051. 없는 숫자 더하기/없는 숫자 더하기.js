// TODO: numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수

// 0~9 까지 숫자 합 - numbers 숫자
function solution(numbers) {
    return 45 - numbers.reduce((acc, cur) => acc + cur, 0);
}