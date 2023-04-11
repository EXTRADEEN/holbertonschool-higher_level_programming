#!/usr/bin/node

const val = parseInt(process.argv[2]);

if (Number.isInteger(val)) {
  console.log('My number: ' + val);
} else {
    console.log('Not an integer')
}
