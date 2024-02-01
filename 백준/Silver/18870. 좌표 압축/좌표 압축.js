const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

[n, arr] = input.map((v) => v.split(' ').map((x) => Number(x)));
n = n[0];

sortedArr = [...arr].sort((a, b) => a - b);

const set = new Set(sortedArr);
uniqueArr = [...set];

const lowerIndex = (arr, target, start, end) => {
  while (start < end) {
    mid = parseInt((start + end) / 2);
    if (arr[mid] >= target) end = mid;
    else start = mid + 1;
  }
  return start;
};

const result = [];
arr.forEach((data, idx) => {
  result.push(lowerIndex(uniqueArr, data, 0, uniqueArr.length - 1));
});

console.log(result.join(' '));
