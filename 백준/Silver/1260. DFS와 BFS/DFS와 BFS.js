function solution(n, v, edges) {
  visited = Array(n + 1).fill(false);
  result = [];
  function dfs(x) {
    visited[x] = true;
    result.push(x);

    for (let data of edges[x]) {
      if (!visited[data]) {
        dfs(data);
      }
    }
  }

  dfs(v);
  console.log(result.join(" "));

  function bfs(x) {
    visited = Array(n + 1).fill(false);
    queue = [x];
    answer = [x];

    visited[x] = 1;
    startIdx = 0;

    while (startIdx < queue.length) {
      let x = queue[startIdx];
      startIdx += 1;

      for (let data of edges[x]) {
        if (!visited[data]) {
          queue.push(data);
          answer.push(data);
          visited[data] = true;
        }
      }
    }

    console.log(answer.join(" "));
  }

  bfs(v);
}

/* readline Module */
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input;

// n, m, v 입력
// 간선 입력
let n, m, v;
let edges;
let count = 0;

rl.on("line", function (line) {
  if (count === 0) {
    input = line;
    [n, m, v] = input.split(" ").map((el) => Number(el));

    edges = Array(n + 1)
      .fill(new Array())
      .map(() => []);
  } else {
    input = line;
    [a, b] = input.split(" ").map((el) => Number(el));
    edges[a].push(b);
    edges[b].push(a);
  }

  if (m && count == m) {
    rl.close(); // 입력 종료
  }

  count += 1;
}).on("close", function () {
  for (let i = 1; i < edges.length; i++) {
    edges[i].sort((a, b) => a - b);
  }

  solution(n, v, edges); // 문제 풀이 함수 호출
  process.exit(); // 프로세스 종료
});
