#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const myDict = {};

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    const response = JSON.parse(body);

    for (let n = 0; n < response.length; n++) {
      if (response[n].completed === true) {
        if (myDict[response[n].userId] === undefined) {
          myDict[response[n].userId] = 1;
        } else {
          myDict[response[n].userId] += 1;
        }
      }
    }
  }
  console.log(myDict);
});
