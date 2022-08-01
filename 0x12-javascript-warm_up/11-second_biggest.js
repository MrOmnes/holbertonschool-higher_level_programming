#!/usr/bin/node

const array = process.argv.sort();
array.reverse();

if (!process.argv[3]) {
  console.log(0);
}

console.log(array[1]);
