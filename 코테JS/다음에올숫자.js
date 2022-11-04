function solution(common) {
    let gap = common[1] - common[0];
    if (gap === common[2] - common[1]){ // 등차
        return common[common.length-1] + gap;
    } else{ // 등비
        return common[common.length-1] * (common[1] / common[0]);
    }
}
