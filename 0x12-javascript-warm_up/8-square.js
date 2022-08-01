#!/usr/bin/node
let i = parseInt(process.argv[2]);
if (!Number.isInteger(i)) {
  console.log('Missing size');
}
if (Math.sign(i) === 1) {
  const j = i;
  while (i) {
    console.log('X'.repeat(j));
    i--;
  }
}
