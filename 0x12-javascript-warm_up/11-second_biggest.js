#!/usr/bin/node

process.argv.shift();
process.argv.shift();
for (let i = 0; i < process.argv.length; i++) {
    process.argv[i] = parseInt(process.argv[i]);
}

const array = process.argv.sort();
if (array.length < 2) {
  console.log(0);
} else {
  array.reverse();

  console.log(array[1]);
}
