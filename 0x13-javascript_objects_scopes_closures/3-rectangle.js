#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      // this. to make the variable public
      this.width = w;
      this.height = h;
    }
  }

  // method to print the rectangle using the character X
  print() {
    let row;
    for (row = 0; row < this.height; row++) {
      console.log("X".repeat(this.width));
    }
  }
};
