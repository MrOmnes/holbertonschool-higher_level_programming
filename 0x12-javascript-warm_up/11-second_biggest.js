#!/usr/bin/node
let i = 2;
let values = [];
if (process.argv[2] === undefined || process.argv[3] === undefined){
	console.log(0);
}
while (process.argv[i] !== undefined) {
	values.push(process.argv[i]);
	i++;
}

console.log(values.sort().reverse()[1]);
