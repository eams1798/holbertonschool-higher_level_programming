#!/usr/bin/node
/**/
const request = require('request');
const URL = process.argv[2];

request(URL, function (err, res, body) {
  if (err) console.log(err);
  else {
    const json = JSON.parse(body);
    const results = {};
    for (let i = 0; i < json.length; i++) {
      const task = json[i];
      if (task.completed === true) {
        if (results[task.userId] !== undefined) {
          results[task.userId] += 1;
        } else {
          results[task.userId] = 1;
        }
      }
    }
    console.log(results);
  }
});
