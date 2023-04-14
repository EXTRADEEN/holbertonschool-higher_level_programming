#!/usr/bin/node

// Module that prints a square and inherits all methods from previous Class

class Square extends require('./5-square') {
  charPrint (c) {
    const char = c || 'X';
    let square = '';
    for (let i = 0; i < this.width; i++) {
      square += char;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(square);
    }
  }
}

module.exports = Square;
