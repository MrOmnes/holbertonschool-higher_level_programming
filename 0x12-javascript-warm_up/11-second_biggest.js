#!/usr/bin/node
let i = 2;
const values = [];
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  while (process.argv[i] !== undefined) {
    if (!values.includes(process.argv[i])) {
      values.push(process.argv[i]);
    }
    i++;
  }

  console.log(values.sort().reverse()[1]);
}
