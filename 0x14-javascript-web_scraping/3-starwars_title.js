#!/usr/bin/node
/**/
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(URL, function (err, res, body) {
  if (err) console.log(err);
  else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
