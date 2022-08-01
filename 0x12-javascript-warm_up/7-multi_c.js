#!/usr/bin/node
let i = parseInt(process.argv[2]);
if (!Number.isInteger(i)) {
  console.log('Missing number of occurences');
}
if (Math.sign(i) === 1) {
  while (i) {
    console.log('C is fun');
    i--;
  }
}
