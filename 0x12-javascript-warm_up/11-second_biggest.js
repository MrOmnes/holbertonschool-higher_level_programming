#!/usr/bin/node

process.argv.shift();
process.argv.shift();

const array = process.argv.sort();
if (array.length < 2) {
  console.log(0);
} else {
  array.reverse();

  console.log(array[1]);
}
