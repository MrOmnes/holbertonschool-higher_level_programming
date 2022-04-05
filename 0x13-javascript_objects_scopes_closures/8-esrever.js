#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  let a = list.length - 1;
  while (list[a] !== undefined) {
    reversed.push(list[a]);
    a--;
  }
  return reversed;
};
