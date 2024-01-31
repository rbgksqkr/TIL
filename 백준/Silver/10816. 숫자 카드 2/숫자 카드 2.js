const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [n, a, m, b] = input.map((v) => v.split(' ').map((x) => Number(x)));

a.sort((a, b) => a - b);

const lowerIndex = (arr, target, start, end) => {
  while (start < end) {
    mid = parseInt((start + end) / 2);
    if (arr[mid] >= target) end = mid;
    else start = mid + 1;
  }
  return start;
};

const upperIndex = (arr, target, start, end) => {
  while (start < end) {
    mid = parseInt((start + end) / 2);
    if (arr[mid] > target) end = mid;
    else start = mid + 1;
  }
  return start;
};

const binarySearch = (target) => {
  const l = lowerIndex(a, target, 0, n[0]);
  const r = upperIndex(a, target, 0, n[0]);
  return r - l;
};

const result = b.map((v) => binarySearch(v));
console.log(result.join(' '));
