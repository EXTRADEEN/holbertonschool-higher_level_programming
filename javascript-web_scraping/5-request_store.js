#!/usr/bin/node

// script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request-promise-native');

const file = process.argv[2];
const fInput = process.argv[3];

request(file, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(fInput, body, 'utf8', err => {
      if (err) throw (err);
    });
  }
});
