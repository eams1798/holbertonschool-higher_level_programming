#!/usr/bin/node
/*
 * imports an array and computes a new array
 */
const list = require('./100-data.js').list;
console.log(list);
const list2 = list.map(x => x * list.indexOf(x));
console.log(list2);
