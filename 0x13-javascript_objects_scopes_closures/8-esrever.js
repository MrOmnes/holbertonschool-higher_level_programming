#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length - 1;
  const newList = [];
  let x = 0;
  while (i >= 0) {
    newList[x] = list[i];
    i--;
    x++;
  }
  return newList;
};
