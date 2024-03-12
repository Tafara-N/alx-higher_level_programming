#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // this. Making the variables public
      this.width = w;
      this.height = h;
    }
  }

  // Printing the rectangle using the character X
  print () {
    let row;
    for (row = 0; row < this.height; row++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Rotating the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Doubling the rectangle values
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
