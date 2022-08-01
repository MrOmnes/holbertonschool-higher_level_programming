#!/usr/bin/node
let i = 1;
let result = 1;

function fact(n){
	i++;
	if (i !== n) {
		result = result * i;
		fact(n);
	}
}

console.log(result)