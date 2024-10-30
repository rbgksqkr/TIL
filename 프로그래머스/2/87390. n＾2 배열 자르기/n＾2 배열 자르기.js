// nxn 배열.
// i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채움
// 1, 2, ... n 행을 모두 이어붙인 1차원 배열 생성
// arr[left] ~ arr[right] 만 남기기

// 1. nxn 배열 생성
// 2. i행 i열까지 배열 채우기
// 3. 1차원 배열 만들기
// 4. left 부터 right slice

// 메모리 초과!! n <= 10^7 = 백만
// 다 만들지말고 n번째 1차원 배열만 만들자

function solution(n, left, right) {
    const ans = [];

    while (left <= right) {
        ans.push(Math.max(Math.floor(left / n), left++ % n) + 1);
    }

    return ans;
}