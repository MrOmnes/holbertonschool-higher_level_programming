#!/usr/bin/node

process.argv.shift();
process.argv.shift();

const array = process.argv.sort().reverse();
if (array.length < 2) {
  console.log(0);
} else {
  console.log(array[1]);
}
