#!/usr/bin/node

// cript that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request-promise-native');

const API = process.argv[2];

request.get(API)
  .then((body) => {
    const films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  })
  .catch((error) => {
    console.error(error);
  });
