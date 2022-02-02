#!/usr/bin/node
/**/
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(URL, function (err, res, body) {
  if (err) console.log(err);
  else {
    const allcharacters = JSON.parse(body).characters;
    for (const chr of allcharacters) {
      request(chr, function (err, res, body) {
        if (err) console.log(err);
        else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
