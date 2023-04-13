#!/usr/bin/node

// Module that prints a Rectangle

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let rectangle = '';
    for (let i = 0; i < this.width; i++) {
      rectangle = rectangle + 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(rectangle);
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
}
module.exports = Rectangle;
