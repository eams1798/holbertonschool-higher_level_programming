#!/usr/bin/node
/*
 * concats 2 files
 */
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

if (file1 !== undefined && file2 !== undefined && file3 !== undefined) {
  fs.readFile(file1, function (err, data) {
    if (err) {
      throw err;
    }
    const content1 = data.toString();
    fs.appendFile(file3, content1, function (err) {
      if (err) {
        throw err;
      }
    });
  });

  fs.readFile(file2, function (err, data) {
    if (err) {
      throw err;
    }
    const content2 = data.toString();
    fs.appendFile(file3, content2, function (err) {
      if (err) {
        throw err;
      }
    });
  });
}
