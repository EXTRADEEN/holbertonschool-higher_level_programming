#!/usr/bin/node

// Module that creates a new class Square that inherits from class Rectangle

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

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
