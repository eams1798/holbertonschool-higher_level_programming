#!/usr/bin/node
/*
 * prints My number: <first argument converted in integer> if the first
 * argument can be converted to an integer
 */
const n = parseInt(process.argv[2]);
if (!isNaN(n)) console.log('My number: ' + n);
else console.log('Not a number');
