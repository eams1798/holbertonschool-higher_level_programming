#!/usr/bin/node
/*
 * defined Square class
 */
const Rectangle = require('./4-rectangle');
 
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    if (c === undefined) super.prompt = 'X';
    else super.prompt = c;
    super.print();
  }
};
