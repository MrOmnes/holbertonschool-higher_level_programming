#!/usr/bin/node

process.argv.shift();
process.argv.shift();
const array = process.argv.sort();
array.reverse();

if (!process.argv[1]) {
  console.log(0);
} else {
  if (!process.argv[2]) {
    console.log(process.argv[0]);
  } else {
    console.log(process.argv[1]);
  }
}
