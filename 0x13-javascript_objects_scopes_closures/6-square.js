#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.carac = 'X';
    }
  }

  print () {
    let i = this.height;
    while (i !== 0) {
      console.log(this.carac.repeat(this.width));
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

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      this.carac = c;
      this.print();
    } else {
      this.print();
    }
  }
}

module.exports = Rectangle;
module.exports = Square;
