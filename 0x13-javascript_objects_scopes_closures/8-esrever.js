#!/usr/bin/node
/*
 * returns the reversed version of a list
 */
exports.esrever = function (list) {
  let rev = new Array();

  for (let i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return (rev);
}
