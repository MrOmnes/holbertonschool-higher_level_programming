#!/usr/bin/node
const numberOne = parseInt(process.argv[2]);
const numberTwo = parseInt(process.argv[3]);
if (!Number.isInteger(numberOne) && !Number.isInteger(numberTwo)) {
  console.log('NaN');
} else {
  console.log(numberOne + numberTwo);
}
