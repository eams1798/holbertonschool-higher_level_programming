#!/usr/bin/node
/*
 * ;searches the second biggest integer in the list of arguments
 */
const listInt = process.argv.slice(2);
if (listInt.length <= 1) console.log('0');
else {
  let i;
  for (i in listInt) {
    listInt[i] = parseInt(listInt[i]);
  }
  const idxMax = listInt.indexOf(Math.max(...listInt));
  listInt.splice(idxMax, 1);
  const secondMax = Math.max(...listInt);
  console.log(secondMax);
}
