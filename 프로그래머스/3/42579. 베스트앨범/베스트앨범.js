// 장르별 가장 많이 재생된 노래 2개씩 베스트 앨범
// 고유 번호로 구분
// 1. 속한 노래가 많이 재생된 장르를 먼저 수록
// 2. 장르 내에서 많이 재생된 노래를 먼저 수록
// 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

// TODO: 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 나열한 배열 반환

// genres: [장르 배열], plays: [노래별 재생 횟수 배열]
// 1. 많이 재생된 장르 순서를 구한다. {"classic": 1450, "pop": 3100} => pop
// 2. 장르 내에서 재생 횟수가 큰 노래 순서를 구한다. {pop: [4, 1], classic: [3, 0, 1]}
// 2-2. 재생횟수가 같다면 고유 번호가 낮은 노래 먼저 수록한다.
// 2-3. 장르에 속한 곡이 1개라면 1개, 2개 초과하면 우선순위에 따라 2개 선별.

// {genre: "classic", index: 0, play: 500}

function solution(genres, plays) {
    var answer = [];
    const n = genres.length;
    
    let data = {};
    for(let i = 0; i < n; i++){
        data[genres[i]] ? data[genres[i]] += plays[i] : data[genres[i]] = plays[i]    
    }
    
    // 1번 : 많이 재생된 순서대로 장르 정렬
    let genreCountArr = Object.entries(data);
    genreCountArr.sort((a, b) => b[1] - a[1])
    
    
    // 2번 : 장르 내에서 재생 횟수가 많은 노래 순서 (같으면 인덱스 작은 순)
    let musics = genres.map((genre, idx) => ({
        genre,
        index: idx,
        playCount: plays[idx]
    }))
    
    // 많이 재생된 장르 순서대로 순회하면서 재생 횟수가 많은 노래 순서대로 answer에 추가
    genreCountArr.forEach((data) => {
        [genre, _] = data;
        const targetMusic = musics.filter((data) => data.genre === genre);
        
        // 2-2. 고유 번호가 낮은 순
        targetMusic.sort((a, b) => a.index - b.index);
        
        // 2-3. 재생횟수 많을 경우만 순서 변경. 아니면 유지해서 고유 번호 낮은 순
        targetMusic.sort((a, b) => b.playCount - a.playCount);
        
        targetMusic.forEach((data, idx) => {
            if(idx >= 2) return;
            answer.push(data.index);  
        })
        
    })
    
    return answer;
}