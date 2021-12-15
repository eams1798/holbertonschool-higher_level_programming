#!/usr/bin/node
/*
 * defined Square class
 */
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) this.prompt = 'X';
    else this.prompt = c;
    super.print();
  }
};
