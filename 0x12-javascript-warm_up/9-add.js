#!/usr/bin/node
/*
 * prints the addition of 2 integers
 */
function add (a, b) {
  return (a + b);
}
const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);
console.log(add(x, y));
