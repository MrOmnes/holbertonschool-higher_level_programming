#!/usr/bin/node
const myVar = 'C is fun';
let i = parseInt(process.argv[2]);
if (Number.isInteger(i) && Math.sign(i) === 1) {
  while (i !== 0) {
    console.log(myVar);
    i--;
  }
}
else if (Number.isInteger(i) && Math.sign(i) !== 1) {
  i--;
} else {
  console.log('Missing number of occurrences');
}
