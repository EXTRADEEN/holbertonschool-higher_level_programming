#!/usr/bin/node

// script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const objID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${objID}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const mov = JSON.parse(body);
  console.log(mov.title);
});
