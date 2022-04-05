#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (width, height) {
    const myVar = 'X';
    let i = this.height;
    while (i !== 0) {
      console.log(myVar.repeat(this.width));
      i--;
    }
  }
}

module.exports = Rectangle;
