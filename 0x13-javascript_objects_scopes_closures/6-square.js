#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const myVar = 'X';
    let i = this.height;
    while (i !== 0) {
      console.log(myVar.repeat(this.width));
      i--;
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = (this.height) * 2;
    this.width = (this.width) * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let myVar = c;
    if (myVar === undefined) {
      myVar = 'X';
    }
    let i = this.height;
    while (i !== 0) {
      console.log(myVar.repeat(this.width));
      i--;
    }
  }
}

module.exports = Rectangle;
module.exports = Square;
