#!/usr/bin/node

// script that writes a string to a file.

const fs = require('fs');
const file = process.argv[2];
const fInput = process.argv[3];

fs.writeFile(file, fInput, 'utf8', (err) => {
  if (err) throw (err);
});
