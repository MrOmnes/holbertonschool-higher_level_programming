#!/usr/bin/node
const myVar = parseInt(process.argv[2]);
let i = 1;
let result = 1;
while (i - 1 !== myVar) {
  result = result * i;
  i++;
}
console.log(result);
