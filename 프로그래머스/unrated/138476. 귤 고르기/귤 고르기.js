function solution(k, tangerine) {
    const types = {};
    tangerine.sort()
    for(let i = 0; i < tangerine.length; i++) {
        if (types[tangerine[i]]) {
            types[tangerine[i]] += 1
        } else {
            types[tangerine[i]] = 1
        }
    }
    const typesArray = [];
    for (let value in types){
        typesArray.push([value, types[value]])
    }
    const result = typesArray.sort(function(a, b) {
        return a[1] - b[1];
    })

    let left = tangerine.length - k;
    let typeLength = 0
    for (let i = 0; i < typesArray.length; i++){
        if (typesArray[i][1] <= left) {
            left -= typesArray[i][1]
            typeLength += 1
        } else {
            break;
        }
    }
    return typesArray.length - typeLength;
}