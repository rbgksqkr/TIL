const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

[a, ...arr] = input;
[k, n] = a.split(' ').map((e) => Number(e));

arr = arr.map((e) => Number(e));
arr.sort((a, b) => a - b);

function solve(x) {
  let cur = 0;
  for (let i = 0; i < k; i++) {
    count = parseInt(arr[i] / x);
    cur += count;
  }

  if (cur >= n) {
    return true;
  } else return false;
}

start = 1;
end = arr[arr.length - 1];
while (start < end) {
  mid = parseInt((start + end + 1) / 2);

  if (solve(mid)) start = mid;
  else end = mid - 1;
}
console.log(start);
