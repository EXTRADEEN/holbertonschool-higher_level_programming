#!/usr/bin/node

const val = parseInt(process.argv[2]);
let i = 0;

if (!Number.isInteger(val)) {
  console.log('Missing number of occurrences');
} else {
  for (;i < val; i++) {
    console.log('C is fun');
  }
}
