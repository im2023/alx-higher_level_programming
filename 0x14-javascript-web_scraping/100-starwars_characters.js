#!/usr/bin/node
const request = require('request');
const endPoint = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(endPoint, function (err, rsp, body) {
  if (err) {
    throw err;
  } else if (rsp.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request.get(character, function (err, rsp, body) {
        if (err) {
          throw err;
        } else if (rsp.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
