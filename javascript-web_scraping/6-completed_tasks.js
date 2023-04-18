#!/usr/bin/node

// script that computes the number of tasks completed by user id

const request = require('request');
const API = process.argv[2];

request.get(API, function (error, response, body) {
  if (error) throw (error);
  const todos = JSON.parse(body);
  const Completed = {};
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].completed === true) {
      if (Completed[todos[i].userId]) {
        Completed[todos[i].userId]++;
      } else {
        Completed[todos[i].userId] = 1;
      }
    }
  }
  console.log(Completed);
});
