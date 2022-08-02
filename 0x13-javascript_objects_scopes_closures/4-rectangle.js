#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (C = 'X') {
    let i = this.height;
    while (i !== 0) {
      console.log(C.repeat(this.width));
      i--;
    }
  }

  rotate () {
    this.temp = this.height;
    this.height = this.width;
    this.width = this.temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};

module.exports = Rectangle;
