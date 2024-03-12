#!/usr/bin/node

const Square5 = require('./5-square');
module.exports = class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; ++i) {
      console.log(c.repeat(this.width));
    }
  }
};
