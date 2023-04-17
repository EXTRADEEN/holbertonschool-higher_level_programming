#!/usr/bin/node

// scrip that reads and prints the content of a file

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', (err, inputD) => {
  if (err) throw (err);
  console.log(inputD.toString());
});
