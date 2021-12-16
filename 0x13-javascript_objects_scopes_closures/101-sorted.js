#!/usr/bin/node
const dict = require('./101-data').dict;

const arrCounter = [];
for (const key in dict) {
  arrCounter.push(dict[key]);
}
const setCount = new Set(arrCounter);

const instanceCounter = {};
// instanceCounter['89'] = [];
for (const s of setCount) {
  instanceCounter[s] = [];
  for (const k in dict) {
    if (dict[k] === s) instanceCounter[s].push(k);
  }
}
console.log(instanceCounter);