#!/usr/bin/node
let i = 2;
let result = 0;
let c = 1;
while (process.argv[i] !== undefined) {
  if (process.argv[i] > result) {
    if (c === 1) {
      result = process.argv[i];
      c++;
    } else {
      c++;
    }
    i++;
  } else {
    i++;
  }
}

console.log(result);
