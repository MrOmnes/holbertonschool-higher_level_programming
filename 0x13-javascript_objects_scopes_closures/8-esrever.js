#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  let a = list.length - 1;
  let i = 0;
  while (list[a] !== undefined) {
    reversed.push(list[a]);
    a--;
    i++;
  }
  return reversed;
};
