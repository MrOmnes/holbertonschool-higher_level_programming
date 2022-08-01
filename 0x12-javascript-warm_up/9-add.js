#!/usr/bin/node
function add (a, b) {
  if (!Number.isInteger(a) && !Number.isInteger(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
