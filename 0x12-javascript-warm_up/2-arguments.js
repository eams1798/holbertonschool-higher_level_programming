#!/usr/bin/node
/*
 * prints a message depending of the number of arguments passed
 */
const nargs = process.argv.length - 2;
if (nargs <= 0) console.log('No argument');
else if (nargs === 1) console.log('Argument found');
else console.log('Arguments found');
