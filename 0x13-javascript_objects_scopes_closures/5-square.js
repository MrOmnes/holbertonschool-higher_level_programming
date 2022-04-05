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

	rotate(){
		let temp = this.height;
		this.height = this.width;
		this.width = temp;
	}

	double(){
		this.height = (this.height) * 2;
		this.width = (this.width) * 2;
	}

  }

class Square extends Rectangle {
	constructor(size){
		super(size, size);
	}
}

module.exports = Rectangle;
module.exports = Square;