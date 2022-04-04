#!/usr/bin/node
const i = parseInt(process.argv[2]);

function factorial (n) {
  if (Number.isInteger(i) === false) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(i));
