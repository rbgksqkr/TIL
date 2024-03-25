const fs = require('fs');
const [n, ...inputs] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
[...data] = inputs.map(input => parseInt(input));

let answer = 0;
for (let i = n - 2; i > -1; i--) {
  if (data[i] >= data[i + 1]) {
    const gap = Math.abs(data[i] - data[i + 1]) + 1;
    answer += gap;
    data[i] -= gap;
  }
}
console.log(answer);