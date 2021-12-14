#!/usr/bin/node
/*
 * prints x times “C is fun”
 */
const x = parseInt(process.argv[2]);
if (isNaN(x)) console.log('Missing number of occurrences');
else {
  if (x > 0) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}
