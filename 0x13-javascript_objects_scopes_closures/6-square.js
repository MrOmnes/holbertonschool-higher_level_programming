#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const character = 'X';
    let i = this.height;
    while (i !== 0) {
      console.log(character.repeat(this.width));
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
    let character = c;
    if (character === undefined) {
        character = 'X';
    }
    let i = this.height;
    while (i !== 0) {
      console.log(character.repeat(this.width));
      i--;
    }
  }
}

module.exports = Rectangle;
module.exports = Square;
