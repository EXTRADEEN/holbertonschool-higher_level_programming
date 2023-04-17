#!/usr/bin/node

// script that displays the status code of a GET request

const request = require('request');
const adress = process.argv[2];

request.get(adress, function (error, response, body) {
  if (!error) {
    console.log('code: ${response.statusCode}');
  }
});
