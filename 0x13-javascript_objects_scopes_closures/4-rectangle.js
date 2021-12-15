#!/usr/bin/node
/*
 * defined Rectangle class
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.prompt = 'X';
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log((this.prompt).repeat(this.width));
    }
  }

  rotate () {
    const w = this.width;
    this.width = this.height;
    this.height = w;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
