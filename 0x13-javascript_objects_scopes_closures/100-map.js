#!/usr/bin/node
const data = require('./100-data');
let i = 0;
const newList = data.list.map(x => x * i++);
console.log(data.list);
console.log(newList);
