// 10초 전. 10초 후. 오프닝 건너뛰기.
// 현재 재생 위치가 오프닝 구간인 경우 오프닝이 끝나는 위치로 이동 (op_start <= 현재 재생 위치 <= op_end)

// TODO: 입력이 끝난 후 동영상의 위치를 "mm:ss" 형식으로 반환

// 1. prev 입력이 오면 10초 전으로 이동. 시작한 시간이 10초 미만이면 시작으로 이동.
// 2. next 입력이 오면 10초 뒤로 이동. 남은 시간이 10초 미만이면 끝으로 이동.
// 3. 이동 후 오프닝 구간이면 오프닝이 끝나는 위치로 이동. 처음 시작 위치가 오프닝 구간이여도 끝나는 위치로 이동 후 이동.

// 분 단위를 계산하기 어려우니 초단위로 변경 후 결과값 반환할 때 다시 되돌리기

function convertSecond(str){
    let [mm, ss] = str.split(':');
    return Number(mm*60) + Number(ss); 
}

function convertStr(number){
    let mm = Math.floor(number / 60).toString().padStart(2, '0');
    let ss = (number % 60).toString().padStart(2, '0');
    return `${mm}:${ss}`;
}

function solution(video_len, pos, op_start, op_end, commands) {
    let newVideoLen = convertSecond(video_len)
    let newPos = convertSecond(pos)
    let newOpStart = convertSecond(op_start)
    let newOpEnd = convertSecond(op_end)
    
    for(let command of commands){
        // 3. 처음 시작 위치가 오프닝 구간이여도 끝나는 위치로 이동 후 이동.
        if(newPos >= newOpStart && newPos <= newOpEnd) {
            newPos = newOpEnd;
        }
        // 1. prev 입력이 오면 10초 전으로 이동. 시작한 시간이 10초 미만이면 시작으로 이동.
        if(command == 'prev'){
            newPos = newPos > 10 ? newPos - 10 : 0;
        }
        // 2. next 입력이 오면 10초 뒤로 이동. 남은 시간이 10초 미만이면 끝으로 이동.
        else if(command == 'next'){
            newPos = newVideoLen-newPos > 10 ? newPos + 10 : newVideoLen;
        }
        
        // 3. 이동 후 오프닝 구간이면 오프닝이 끝나는 위치로 이동. 
        if(newPos >= newOpStart && newPos <= newOpEnd) {
            newPos = newOpEnd;
        }
    }
    
    return convertStr(newPos);
}