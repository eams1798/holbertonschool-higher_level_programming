#!/usr/bin/node
/**/
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const filename = process.argv[3];

request(URL, function (err, res, body) {
  if (err) console.log(err);
  else {
    const content = body;
    fs.writeFile(filename, content, function (err) {
      if (err) console.log(err);
    });
  }
});
