const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [n, a, m, b] = input.map((v) => v.split(' ').map((x) => Number(x)));

a.sort((a, b) => a - b);

const binarySearch = (arr, target, start, end) => {
  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    if (arr[mid] === target) {
      return 1;
    } else if (arr[mid] > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return 0;
};

const result = b.map((target) => binarySearch(a, target, 0, n - 1));
console.log(result.join('\n'));
